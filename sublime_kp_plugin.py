# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See the COPYING file for more details.

import sublime, sublime_plugin

class KpEventListener(sublime_plugin.EventListener):
	def on_load(self, view):
		if (self.isKpFile(view)):
			view.run_command("reopen", {"encoding": "Central European (ISO 8859-2)" })

	def on_pre_save(self, view):
		if (self.isKpFile(view)):
			view.set_encoding("Central European (ISO 8859-2)")
					
	def isKpFile(self, view):
		fileName = view.file_name()

		# here is the super duper way to figure out if it's a KP file
		if (fileName and fileName.lower().endswith('.kp')):
			return True

		return False