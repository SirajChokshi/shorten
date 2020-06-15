import click
import requests
import pyperclip
import json

HOST = "https://s5n.herokuapp.com"

@click.command()
@click.argument('url')
@click.option('-a', '--alias', default=None, help='optional custom alias')
@click.option('-c', '--copy', is_flag=True, help='copy shortened URL to clipboard')
def getShortURL(url, alias, copy):

    req = None
 
    if (alias == None):
        try:
            req = requests.post('{}/api/create?url={}'.format(HOST, url))
        except requests.ConnectionError:
            click.secho("⚠ Connection Refused", fg="red", bold=True)
            return
    else:
        try:
            req = requests.post('{}/api/create?url={}&code={}'.format(HOST, url, alias))
        except requests.ConnectionError:
            click.secho("⚠ Connection Refused", fg="red", bold=True)
            return

    if req.ok:
        res = json.loads(req.content)
        if isinstance(res["shortenedUrl"], int):
            if res["shortenedUrl"] == -1:
                click.secho("\n⚠ Invalid URL", fg="red", bold=True)
                click.secho("Use --help for more information", fg="white")
            elif res["shortenedUrl"] == -2:
                click.secho("\n⚠ Alias is already in use.", fg="red", bold=True)
                click.secho("Use --help for more information", fg="white")
            elif res["shortenedUrl"] == -3:
                click.secho("\n⚠ Invalid alias", fg="red", bold=True)
                click.secho("Use --help for more information", fg="white")
            else:
                click.secho("\n⚠ Unexpected Error", fg="red", bold=True)
        else:
            click.echo("\n" + click.style("Your shortened URL → ", fg="white", bold=True) + click.style(res["shortenedUrl"], fg='magenta', underline=True))
            if copy:
                pyperclip.copy(res["shortenedUrl"])
                click.secho("✔ Copied to Clipboard!", fg='green')
    else:
        click.secho("Server Error: Code {}".format(req.status_code), fg="red", bold=True)

if __name__ == '__main__':
    getShortURL()