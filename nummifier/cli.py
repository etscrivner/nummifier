# -*- coding: utf-8 -*-
import click

import nummifier
import systems
import database


def get_matching_entries(db, number):
    results = []
    for each in db.get_entries(number):
        results.append(each)
    return results


@click.group()
def cli():
    pass


@cli.command()
@click.option('--commit/--no-commit', default=False)
@click.argument('text')
def nummify(commit, text):
    """Console script for nummifier"""
    result = nummifier.nummify_string(text, systems.qa_nummify_character)
    click.echo(text)
    click.echo(result)
    click.echo(sum(result))

    reductions = []
    with database.NummifyDatabase('results.db') as db:
        reduction = sum(result)

        if commit:
            db.add_entry(text, reduction)

        reductions.append(reduction)

        while reduction > 9:
            reduction = nummifier.plex(reduction)
            reductions.append(reduction)

            if commit:
                db.add_entry(text, reduction)

            click.echo(reduction)

        click.echo("")
        for each in reductions:
            results = get_matching_entries(db, each)
            for msg, num in results:
                click.echo("{}={}".format(num, msg))
            click.echo("")


@cli.command()
@click.argument('number')
def search(number):
    with database.NummifyDatabase('results.db') as db:
        for each in db.get_entries(number):
            click.echo("{}={}".format(each[1], each[0]))


if __name__ == "__main__":
    cli()
