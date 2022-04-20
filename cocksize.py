class enum:
	def __init__(self,*args):
		cnt = 0
		for prop in args:
			setattr(self, prop, cnt)
			cnt += 1
