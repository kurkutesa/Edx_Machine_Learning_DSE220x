class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if not user:
            html = '<html><body>'
	    html = html + '<center><h1>Voting Website</h1></center>'
	    html = html + ('<center><a href=\"%s\">Sign in or register</a></center>'% (users.create_login_url("/")))
	    html = html + '</body></html>'
        else:
            self.storeUser(user.nickname())
	    welcomeString = ('<p>Welcome, %s! </p>'% user.nickname())
	    signOutString = ('<a href="%s">sign out</a>'% users.create_logout_url("/"))
	    html = template.render('template/page_begin.html', {})
	    html = html + '<div id="content" style="width:60%; height:100%; float:left">'
	    html = html + '<center>' + welcomeString + '</center><br>'
	    html = html + '</div>'
	    html = html + '<div id="sidebar" style="width:20%; height:100%; float:right; background-color:grey">'
	    html = html + '<center>' + signOutString + '</center><br><br>'
	    html = html + '<form action="/search" method="post">'
	    html = html + '<input type="text" name="searchItem">'
	    html = html + '<input type="submit" name="button" value="Search"></form>'
	    html = html + '</div>'
	    html = html + template.render('template/page_end.html', {})
	    self.response.out.write(html)

