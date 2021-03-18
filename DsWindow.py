import inspect
import PySimpleGUI as sg
import DsTools


class WindowBase:
    Result = DsTools.Result.ID_OK
    def __init__(self):
        pass
    def show(self):
        pass

class ControlParamWindow(WindowBase):
    def __init__(self):
        return
    def show(self):
        stepcontrol = sg.Frame(
            'Step control',
            [[sg.Text('Current Step No.'),
              sg.Text("phy", size=(10,1), relief=sg.RELIEF_RIDGE),
              sg.Button('<-'), sg.Button('->')]])
        layout = [[stepcontrol]]
        window = sg.Window('ControlParamWindow', layout, modal=True)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'OK':
                break
        window.close()

class CalibrationWindow(WindowBase):
    def __init__(self):
        return

    def show(self):
        buttons = [sg.Button('Update Variables', size=(21,1)),
                                   sg.Button('Load From File', size=(21,1)),
                                   sg.Button('Save To File', size=(21,1)),
                                   sg.Button('Close', size=(21,1))]
        factors = []
        for ch in range(0, DsTools.Define.MAX_CH):
            factors.append(
                [sg.Text('CH %02d' % ch, size=(20,1)),
                 sg.Input(size=(10,1)), sg.Text('*x^2+'),
                 sg.Input(size=(10,1)), sg.Text('*x^1+'),
                 sg.Input(size=(10,1)), sg.Text('='),
                 sg.Text("phy", size=(10,1), relief=sg.RELIEF_RIDGE),
                 sg.Button('Zero'), sg.Button('Apply')])
        factors_frame = [sg.Frame('Calibration Factors', factors)]
        layout = [buttons, factors_frame]
        window = sg.Window('CalibrationWindow', layout, modal=True)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'OK':
                break
        window.close()

class MainWindow(WindowBase):
    def __init__(self):
        return

    def show(self):
        sg.theme('Dark')   # Add a touch of color
        raws = []
        for ch in range(0, DsTools.Define.MAX_CH):
            raws.append([sg.Text('CH %02d' % ch), sg.Text('0x1234ABCD', text_color='black', background_color='white')])
        raws_frame = sg.Column([[sg.Frame('Raw Data', raws)]])

        voltages = []
        for ch in range(0, DsTools.Define.MAX_CH):
            voltages.append(
                [sg.Text('CH %02d' % ch), sg.Text('+00.0000', text_color='black', background_color='white')])
        voltages_frame = sg.Column([[sg.Frame('Voltage Output', voltages)]])

        phisicals = []
        for ch in range(0, DsTools.Define.MAX_CH):
            phisicals.append(
                [sg.Text('CH %02d Pysic' % ch), sg.Text('+000000.0000', text_color='black', background_color='white')])
        phisicals_frame = sg.Column([[sg.Frame('Phisicals Value Output', phisicals)]])

        params = []
        for ch in range(0, DsTools.Define.MAX_CH):
            params.append([
                sg.Text('param [Unit]'),
                sg.Text('+000000.0000', text_color='black', background_color='white'),
                sg.Text('param [Unit]'),
                sg.Text('-000000.0000', text_color='black', background_color='white')
            ])
        params_frame = sg.Column([[sg.Frame('Parameter of Static Pysical-Value', params)]])

        # Create the Window
        layout = [[raws_frame, voltages_frame, phisicals_frame, params_frame]]
        window = sg.Window('DigitShowPython', layout, modal=True)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break

        window.close()

class VersionWindow(WindowBase):
    def __init__(self):
        return

    def show(self):
        layout = [[sg.Text('Application Version'), sg.Button('OK')]]
        window = sg.Window('VersionWindow', layout, modal=True)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'OK':
                break
        window.close()

class DebugWindow(WindowBase):
    def __init__(self):
        return

    def onPushVersionWindow(self):
        print(inspect.currentframe().f_code.co_name)
        VersionWindow().show()

    def show(self):
        sg.theme('Dark')
        layout = [
            [sg.Button('VersionWindow', key=lambda: VersionWindow().show())],
            [sg.Button('PopupWindow', key=lambda: sg.popup('PopUp Test'))],
            [sg.Button('MainWindow', key=lambda: MainWindow().show())],
            [sg.Button('CalibrationWindow', key=lambda: CalibrationWindow().show())],
            [sg.Button('ControlParamWindow', key=lambda: ControlParamWindow().show())],
        ]
        window = sg.Window('VersionWindow', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif callable(event):
                event()

        window.close()