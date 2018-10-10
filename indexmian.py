from sql import Sql

class Index (object):

	def selectuser(user ,password):
		if user == None and password == None :
			return 'login'
		if user != '' and password != '' :
			s = Sql()
			re = s.select(userName = user)
			for r in re:
				u = r[0]
				p = r[1]
				t = r[2]
		
			if user == u and password == p :
				return 1
		else :
			return 0
