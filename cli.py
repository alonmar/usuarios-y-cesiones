#!/usr/bin/env python
import click
from mlib import predict

#var=

@click.command()
@click.option(
    '--monactivo',
    type=click.FLOAT,
    prompt="Monto activo",
    help="Pass the Monto activo of a user",
)
@click.option(
    '--meansales',
    type=click.FLOAT,
    prompt="Promedio Ventas",
    help="Pass the Promedio Ventas of a user",
)
@click.option(
    '--meancesiones', 
    type=click.FLOAT,
    prompt="Promedio Cesiones",
    help="Pass the Promedio Cesiones of a user",
)
@click.option(
    '--proyecsales', 
    type=click.FLOAT,
    prompt="Proyeccion ventas",
    help="Pass the Proyeccion ventas of a user",
)
@click.option(
    '--proyecbuys',
    type=click.FLOAT,
    prompt="Proyeccion compras",
    help="Pass the Proyeccion compras of a user",
)
def predictcli(monactivo, meansales, meancesiones, proyecsales, proyecbuys):    
    """Predicts cluster of an user"""

    data_to_predict = {
        'Monto activo': monactivo, 
        'Promedio Ventas': meansales, 
        'Promedio Cesiones': meancesiones, 
        'proyeccion ventas': proyecsales, 
        'proyeccion compras': proyecbuys}

    result = predict(data_to_predict)
    
    if result == 0:
        click.echo(click.style(f'Cluster: {result}', bg="green", fg="black"))
    elif result == 1:
        click.echo(click.style(f'Cluster: {result}', bg="red", fg="black"))
    elif result == 2:
        click.echo(click.style(f'Cluster: {result}', bg="magenta", fg="black"))
    elif result == 3:
        click.echo(click.style(f'Cluster: {result}', bg="yellow", fg="black"))
    elif result == 4:
        click.echo(click.style(f'Cluster: {result}', bg="blue", fg="black")) 


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    predictcli()