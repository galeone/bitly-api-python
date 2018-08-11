import urllib
from io import StringIO


class DontRedirect(urllib.request.HTTPRedirectHandler):

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if code in (301, 302, 303, 307):
            raise urllib.HTTPError(req.get_full_url(), code, msg, headers, fp)


def makeUrllib2Http(url, user_agent):
    dont_redirect = DontRedirect()
    opener = urllib.request.build_opener(dont_redirect)
    opener.addheaders = [('User-agent', user_agent + ' urllib')]

    try:
        response = opener.open(url)
        code = response.code
        data = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        return 500, str(e)
    except urllib.error.HTTPError as e:
        code = e.code
        data = e.read()
    return code, data


def get(url, timeout, user_agent):
    code, result = makeUrllib2Http(url, user_agent)
    return {'http_status_code': code, 'result': result}
