# -*- coding: utf-8 -*-

import xbmc
import xbmcgui


if __name__ == '__main__':
    redirect_uri = "http://rawgit.com/tamland/kodi-oauth-demo/master/web-client/index.html"

    url = "https://github.com/login/oauth/authorize?" \
          "client_id=015a99a34e503b183240&" \
          "scope=&" \
          "state=123&" \
          "redirect_uri=" + redirect_uri

    xbmc.requestAuthorization(url)

    dialog = xbmcgui.DialogProgress()
    dialog.create('Authorizing...')

    for i in range(0, 100):
        if dialog.iscanceled():
            break

        response = xbmc.getResponse()
        if response != "":
            dialog.close()
            xbmc.log("Got response: " + response)
            xbmcgui.Dialog().ok("Got response", response.split('?')[-1])
            break

        xbmc.sleep(1000)
        dialog.update(i + 1)
