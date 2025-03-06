def run(Lime):
    Lime.Log.debug("hi")
    Lime.Log.error("error")


moduleInfo = {
    "name": "Test2",
    "description": "This is a test module (again)",
    "canBeUndone": False,
    "run": run,
    "canRerun": True,
    "verbose": False,
    "os": "win"
}
