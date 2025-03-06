def run(Lime):
    Lime.Log.debug("you can't see this")
    Lime.Log.warn("yo error might happen")

def undo(Lime):
    Lime.Log.success("success")

moduleInfo = {
    "name": "Test1",
    "description": "This is a test module",
    "canBeUndone": True,
    "run": run,
    "undo": undo,
    "canRerun": False,
    "verbose": False,
    "os": "win"
}
