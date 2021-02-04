import click

from . import str2port


@click.command()
@click.argument('string')
@click.option('--use-iana', is_flag=True, help='Exclude used ports from IANA list (default: false)')
@click.option('--start', default=1024)
@click.option('--end', default=65536)
def cli(string, use_iana, start, end):
    click.echo(' '.join(str(i) for i in str2port(string, use_iana, start, end)))


if __name__ == '__main__':
    cli()
