from enum import Enum
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle, RoundedRectangle, Line
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

from GolfTees import CreateTriangleBoard

class AppState(Enum):
	Ready = 1
	Running = 2
	Paused = 3
	Finished = 5

nextState={
	AppState.Ready: AppState.Running,
	AppState.Running: AppState.Paused,
	AppState.Paused: AppState.Running,
	AppState.Finished: AppState.Ready
	}


class Speed(Enum):
	Slow=1
	Medium=2
	Fast=3

nextSpeed={
	Speed.Slow: Speed.Medium,
	Speed.Medium: Speed.Fast,
	Speed.Fast: Speed.Slow
	}

class SpeedInfo:
	def __init__(self, statusText='', fps=0):
		self.statusText=statusText
		self.fps=fps

infoFromSpeed = {
	Speed.Slow: SpeedInfo(statusText='Slow', fps=1),
	Speed.Medium: SpeedInfo(statusText='Medium', fps=10),
	Speed.Fast: SpeedInfo(statusText='High', fps=100)
	}

class ButtonInfo:
	def __init__(self, enabled=True, text=''):
		self.enabled = enabled
		self.text=text

class AppInfo:
	def __init__(self, statusText='', 
							startInfo=ButtonInfo(),
							speedInfo=ButtonInfo()):
		self.statusText=statusText
		self.startInfo=startInfo
		self.speedInfo=speedInfo

infoFromState = {
	AppState.Ready: AppInfo(statusText='Ready', 
												 startInfo=ButtonInfo(text='Start', enabled=True),
												 speedInfo=ButtonInfo(text='Change Speed', enabled=True)),
	AppState.Running: AppInfo(statusText='Running', 
												 startInfo=ButtonInfo(text='Pause', enabled=True),
												 speedInfo=ButtonInfo(text='Change Speed', enabled=False)),
	AppState.Paused: AppInfo(statusText='Paused', 
												 startInfo=ButtonInfo(text='Resume', enabled=True),
												 speedInfo=ButtonInfo(text='Change Speed', enabled=True)),
	AppState.Finished: AppInfo(statusText='Done', 
												 startInfo=ButtonInfo(text='Reset', enabled=True),
												 speedInfo=ButtonInfo(text='Change Speed', enabled=False))
	}


class RoundedRectLabel(Label):
	"""
	Creates a rounded rectangle whose color can be changed. 
	Possibly should be based on a button in the long run.
	"""
	def __init__(self, text_color=[0.0, 0.0, 0.0, 1.0], back_color=[1.0, 1.0, 1.0, 1.0], **kwargs):
		super().__init__(color=text_color, **kwargs)
		self.back_color = back_color
		self.CreateBackground(back_color, force=True)
		self.bind(pos=self.update_rect, size=self.update_rect)
		return

	def CreateBackground(self, color=[1,1,1,1], force=False):
		if force or self.back_color != color:
			self.back_color = color
			self.canvas.before.clear()
			with self.canvas.before:
				Color(color[0], color[1], color[2], color[3])
				self.background = RoundedRectangle(size=self.size, pos=self.pos)

	def update_rect(self, instance, value):
		self.background.pos = instance.pos
		self.background.size = instance.size
		self.font_size = instance.size[1]/2
		return

	def SetColors(self, text_color=[0.0, 0.0, 0.0, 1.0],
							 back_color=[1.0, 1.0, 1.0, 1.0]):
		self.color = text_color
		self.CreateBackground(back_color)


# BoardLayout encapsulates the playing board
class BoardLayout(BoxLayout):
	def __init__(self, board):
		super().__init__()
		self.MakeBoard(board)
		self.bind(pos=self.update_rect, size=self.update_rect)

	def MakeBoard(self, board):
		self.pegHoles = []
		if len(board.holes) > 0:
			self.minRow = min([hole.row for hole in board.holes])
			self.maxRow = max([hole.row for hole in board.holes])
			self.minCol = min([hole.col for hole in board.holes])
			self.maxCol = max([hole.col for hole in board.holes])

			for hole in board.holes:
				newPegHole = RoundedRectLabel(text_color = [0, 0, 0, 1], back_color = [1, 0, 0, 1])
				newPegHole.hole = hole
				self.add_widget(newPegHole)
				self.pegHoles.append(newPegHole)
		return

	def update_rect(self, instance, value):
		# instance.rect.pos = instance.pos
		# instance.rect.size = instance.size
		pass

class HeaderLayout(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(orientation='horizontal', **kwargs)
		self.PlaceStuff()
		self.bind(pos=self.update_rect, size=self.update_rect)

	def PlaceStuff(self):
		with self.canvas.before:
			Color(0.6, .6, 0.1, 1)  # yellow; colors range from 0-1 not 0-255
			self.rect = Rectangle(size=self.size, pos=self.pos)
		textColor = [0.7,0.05, 0.7, 1]
		self.speedLabel = Label(text='Animation speed: ', color=textColor)
		self.add_widget(self.speedLabel)
		self.statusLabel = Label(text='Ready', color = textColor)
		self.add_widget(self.statusLabel)
		self.fpsLabel = Label(text='0 fps', color=textColor)
		self.add_widget(self.fpsLabel)
		
	def UpdateText(self, fps=0, statusText='Ready', speedText=''):
		self.speedLabel.text='Speed: {speed}'.format(speed=speedText)
		self.fpsLabel.text = '{fpsValue:.0f} fps'.format(fpsValue=fps)
		self.statusLabel.text = statusText.format()

	def update_rect(self, instance, value):
		instance.rect.pos = instance.pos
		instance.rect.size = instance.size


class FooterLayout(BoxLayout):
	def __init__(self, 
							start_button_callback=None, 
							speed_button_callback=None, 
							**kwargs):
		super().__init__(orientation='horizontal', padding=10, **kwargs)
		self.start_button_callback=start_button_callback
		self.speed_button_callback=speed_button_callback
		self.PlaceStuff()
		self.bind(pos=self.update_rect, size=self.update_rect)

	def PlaceStuff(self):
		with self.canvas.before:
			Color(0.4, .1, 0.4, 1)  # purple; colors range from 0-1 not 0-255
			self.rect = Rectangle(size=self.size, pos=self.pos)
		
		self.speedButton = Button()
		self.add_widget(self.speedButton)
		self.speedButton.bind(on_press=self.speed_button_callback)
		self.startButton = Button()
		self.add_widget(self.startButton)
		self.startButton.bind(on_press=self.start_button_callback)
		self.UpdateButtons()

	def update_rect(self, instance, value):
		instance.rect.pos = instance.pos
		instance.rect.size = instance.size

	def UpdateButtons(self, appInfo=infoFromState[AppState.Ready]):
		startInfo = appInfo.startInfo
		self.startButton.text = startInfo.text
		self.startButton.disabled = not startInfo.enabled
		speedInfo = appInfo.speedInfo
		self.speedButton.text=speedInfo.text
		self.speedButton.disabled = not speedInfo.enabled


class GolfTeesGame(App):
	def build(self):
		self.root = layout = BoxLayout(orientation = 'vertical')
		self.state = AppState.Ready
		self.clock=None
		self.generator=None
		self.simulationLength = 500
		self.rotationShift = 150
		self.array = list(range(self.simulationLength))
		self.speed = Speed.Slow
		self.gameBoard = CreateTriangleBoard(4)

		# header
		self.header = HeaderLayout(size_hint=(1, .1))
		layout.add_widget(self.header)

		# board
		self.board = BoardLayout(self.gameBoard)
		layout.add_widget(self.board)

		# footer
		self.footer = FooterLayout(size_hint=(1, .2), 
														 start_button_callback=self.StartButtonCallback,
														 speed_button_callback=self.SpeedButtonCallback)
		layout.add_widget(self.footer)

		self.UpdateUX()
		return layout

	def FrameN(self, dt):
		if self.generator is None:
			return
		if dt != 0:
			fpsValue = 1/dt
		else:
			fpsValue = 0
		if (self.state==AppState.Finished or self.state==AppState.Ready):
			return

		try:
			if self.generator is not None:
				result = next(self.generator)
			self.boardLayout.UpdateColors(self.array)
			self.UpdateUX(fps=fpsValue)
		except StopIteration:
			self.state=AppState.Finished
			self.clock.cancel()
			self.generator=None
			self.UpdateUX(fps=fpsValue)

	def UpdateUX(self, fps=0):
		state = self.state
		speed = self.speed
		appInfo = infoFromState[self.state]
		self.header.UpdateText(fps = fps, 
												 statusText=appInfo.statusText, 
												 speedText=infoFromSpeed[speed].statusText)
		self.footer.UpdateButtons(appInfo=appInfo)

	def StartClock(self):
			self.clock = Clock.schedule_interval(self.FrameN, 
																				1.0/infoFromSpeed[self.speed].fps)

	def StartButtonCallback(self, instance):
		if self.state==AppState.Ready:
			self.array = list(range(self.simulationLength))
			self.StartClock()
		if self.state==AppState.Running:
			self.clock.cancel()
		if self.state==AppState.Paused:
			self.StartClock()
		if self.state==AppState.Finished:
			self.array = list(range(self.simulationLength))
			self.boardLayout.UpdateColors(self.array)
		self.state = nextState[self.state]
		self.UpdateUX()

	def SpeedButtonCallback(self, instance):
		self.speed = nextSpeed[self.speed]
		self.UpdateUX()


def Main():
	GolfTeesGame().run()

if __name__ == '__main__':
	Main()



