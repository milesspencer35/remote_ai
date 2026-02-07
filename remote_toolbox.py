from tools import ToolBox

remote_toolbox = ToolBox()

@remote_toolbox.tool
def volume_up():
    """
    Call this function to increase the volume
    """
    print("Called volume up")

@remote_toolbox.tool
def volume_down():
    """
    Call this function to decrease the volume
    """
    print("Called volume down")

@remote_toolbox.tool
def pause():
    """
    Call this function to pause the video
    """
    print("Called pause")