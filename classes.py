class Oper:
	def __init__(self,type,token,**kwargs):
		self.type = type
		self.token = token
		self.arg = kwargs.get("arg")
		self.jmp = kwargs.get("jmp")
		self.end = kwargs.get("end")

class Token:
	def __init__(self,loc,type,value):
		self.loc = loc
		self.type = type
		self.value = value
