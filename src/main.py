import pyautogui
import os

pyautogui.PAUSE = .5

class MSLAutomationCore:
    """
        Automation for MSL in MuMu Player 12.
    """
    __images_path = ('src','images')
    __dir:tuple

    def __init__(self):
        """
            Load files from `src/images` directory.
        """
        # file_paths = []
        # for file_path in os.listdir(self.getrootpath()):
        #     file_paths.append(self.__getfilepath__(file_path))
        self.__dir = tuple(os.listdir(self.getrootpath()))

    def getrootpath(self):
        """
            Transform immutable images path into a proper path.
        """
        return '/'.join(self.__images_path)
    
    def getfiles(self):
        """
            Returns the collected file names.
        """
        return self.__dir
    
    def navigateto(
            self, 
            filename:str, 
            throw_error:bool=None, 
            image_confidence:float=0.9,
            timeoutInSeconds:int=4,
            event:str='click'
        ):
        """
            This will throw pyautogui.ImageNotFoundException in error.
            event - `click` | `double_click` | `locate`
        """
        image_dictionary = {
            "apex-battles": self.__getfilepath('apex-battles.png'),
            "aria-lake": self.__getfilepath('aria-lake.png'),
            "aurora-plateau": self.__getfilepath('aurora-plateau.png'),
            "auto-battle": self.__getfilepath('auto-battle.png'),
            "back": self.__getfilepath('back.png'),
            "capture-success": self.__getfilepath('capture-success.png'),
            "catch": self.__getfilepath('catch.png'),
            "clan-notice-exit-button": self.__getfilepath('clan-notice-exit-button.png'),
            "cottontails": self.__getfilepath('cottontails.png'),
            "dispatch": self.__getfilepath('dispatch.png'),
            "dungeons": self.__getfilepath('dungeons.png'),
            "emulator-relative-reference": self.__getfilepath('emulator-relative-reference.png'),
            "exit-stages-details": self.__getfilepath('exit-stages-details.png'),
            "exp-bonus-stage": self.__getfilepath('exp-bonus-stage.png'),
            "expedition": self.__getfilepath('expedition.png'),
            "file-explorer": self.__getfilepath('file-explorer.jpg'),
            "glacial-plains": self.__getfilepath('glacial-plains.png'),
            "lunar-valley": self.__getfilepath('lunar-valley.png'),
            "magma-crags": self.__getfilepath('magma-crags.png'),
            "mirage-ruins": self.__getfilepath('mirage-ruins.png'),
            "no-mode-capture": self.__getfilepath('no-mode-capture.png'),
            "normal-speed": self.__getfilepath('normal-speed.png'),
            "normal-stage-final-round": self.__getfilepath('normal-stage-final-round.png'),
            "pagos-coast": self.__getfilepath('pagos-coast.png'),
            "phantom-forest": self.__getfilepath('phantom-forest.png'),
            "play": self.__getfilepath('play.png'),
            "quick-restart": self.__getfilepath('quick-restart.png'),
            "seabed-caves": self.__getfilepath('seabed-caves.png'),
            "shady-shop": self.__getfilepath('shady-shop.png'),
            "skip-dialogue": self.__getfilepath('skip-dialogue.png'),
            "sky-falls": self.__getfilepath('sky-falls.png'),
            "slumbering-city": self.__getfilepath('slumbering-city.png'),
            "stage-battle": self.__getfilepath('stage-battle.png'),
            "stage-clear": self.__getfilepath('stage-clear.png'),
            "star-sanctuary": self.__getfilepath('star-sanctuary.png'),
            "tower-of-chaos": self.__getfilepath('tower-of-chaos.png'),
        }
        try:
            print(filename.upper())
            x, y = pyautogui.locateCenterOnScreen(image_dictionary.get(filename), confidence=image_confidence, minSearchTime=timeoutInSeconds)
            if event == 'double_click':
                return pyautogui.doubleClick(x, y, interval=2)
            if event == 'click':
                return pyautogui.click(x, y)
            if event == 'locate':
                return (x, y)
        except pyautogui.ImageNotFoundException as infe:
            print('%s is not present in the game.' % filename.upper())
            if throw_error == True:
                raise infe
            
    def skipdialouge(self):
        """
            Continuously attempt to skip dialogue until error.
        """
        # If using to brand new device, necessary to press skip.
        try:
            while True:
                
                self.navigateto('skip-dialogue', True)
                self.navigateto('clan-notice-exit-button', True)
        except:
            print('Passing Skip dialouge error, no more skips found.')
            pass
    
    def __getfilepath(self, filename:str):
        index = -1
        rootpath = self.getrootpath()
        try:
            index = self.__dir.index(filename)
        except ValueError:
            error = 'Filename doesn\'t exists in %s' % rootpath
            print(error)
        if index < 0:
            return rootpath
        
        return '/'.join((*self.__images_path, self.__dir[index]))

def main():
    mslac = MSLAutomationCore()
    # [GO TO ADVENTURE]
    # mslac.navigateto('play')
    # mslac.skipdialouge()

    # first_region_stages = ('phantom-forest', 'lunar-valley', 'aria-lake', 'mirage-ruins')
    # second_region_stages = ('pagos-coast', 'seabed-caves', 'magma-crags', 'star-sanctuary')
    # third_region_stages = ('sky-falls', 'slumbering-city', 'glacial-plains', 'aurora-plateau')

    # for stage in first_region_stages:
    #     mslac.navigateto('play', event='double_click')
    #     mslac.skipdialouge()
    #     mslac.navigateto(stage)
    #     mslac.navigateto('exit-stages-details')
    #     mslac.navigateto('back',image_confidence=0.7)

    # # [REGION NAVIGATION]
    # x, y = mslac.navigateto('emulator-relative-reference', event='locate')

    # # [SECOND REGION]
    # for stage in second_region_stages:
    #     mslac.navigateto('play', event='double_click')
    #     mslac.skipdialouge()
    #     pyautogui.moveTo(x+600,y+200)
    #     pyautogui.dragTo(x, None, duration=.5, tween=pyautogui.easeInOutQuad)
    #     mslac.navigateto(stage)
    #     mslac.navigateto('exit-stages-details')
    #     mslac.navigateto('back',image_confidence=0.7)

    # # [THIRD REGION]
    # for stage in third_region_stages:
    #     mslac.navigateto('play', event='double_click')
    #     mslac.skipdialouge()
    #     pyautogui.moveTo(x+800,y+200)
    #     pyautogui.dragTo(x-525, None, duration=.5, tween=pyautogui.easeInOutQuad)
    #     mslac.navigateto(stage)
    #     mslac.navigateto('exit-stages-details')
    #     mslac.navigateto('back',image_confidence=0.7)

    # [ARIA LAKE FARM]
    # mslac.navigateto('play', event='double_click')
    # mslac.skipdialouge()
    mslac.navigateto('aria-lake')
    mslac.navigateto('exp-bonus-stage')
    mslac.navigateto('stage-battle')

    # SET AUTO-BATTLE x4 SPEED.
    # box = mslac.navigateto('normal-speed', timeoutInSeconds=10, event='locate')
    # if box != None:
    #     x,y = box
    #     for _ in range(4):
    #         pyautogui.click(x,y,interval=0.5)

    stage_loop = True
    # mslac.navigateto('auto-battle')

    while stage_loop:
        final_round = mslac.navigateto('normal-stage-final-round', timeoutInSeconds=10, event=
                        'locate', image_confidence=1)
        
        while final_round != None:
            mslac.navigateto('auto-battle')
            capture_location = mslac.navigateto('catch', event='locate', timeoutInSeconds=10)

            if capture_location == None:
                mslac.navigateto('auto-battle')
                break

            pyautogui.click(capture_location[0],capture_location[1])
            monster_location = mslac.navigateto('cottontails', timeoutInSeconds=5, event=
                                'locate')
            if monster_location != None:
                x,y = monster_location
                pyautogui.click(x,y, event='double_click')
            mslac.navigateto('capture-success', timeoutInSeconds=10)
        
        stage_clear = mslac.navigateto('stage-clear', timeoutInSeconds=10, event='locate')
        if stage_clear != None:
            x,y = stage_clear
            pyautogui.doubleClick(x,y, interval=1)
            pyautogui.doubleClick(x,y, interval=2)
            pyautogui.click(x,y)
            mslac.navigateto('quick-restart')
            stage_loop = False


if __name__ == "__main__":
    main()