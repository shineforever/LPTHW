#! /usr/bin/env python
#coding:utf-8

import web


urls = (
        '/hello','Index'
        )


app = web.application(urls,globals())

render = web.template.render('/usr/local/LPTHW/ex51/gothonweb/templates/',base="layout")



class Index(object):
    def GET(self):

        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody",greet="Hello")

        greeting = "%s,%s" % (form.greet,form.name)

        return render.index(greeting = greeting)



if __name__ == '__main__':
    app.run()

