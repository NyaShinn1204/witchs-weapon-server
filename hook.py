import frida, sys
hook_command = open("frida.js", encoding="utf-8").read()
device = frida.get_usb_device()
pid = device.spawn(["com.dmm.games.witchsweapon.google"])
session = device.attach[pid]
script = session.create_script(hook_command)
script.load()
device.resume(pid)
sys.stdin.read()