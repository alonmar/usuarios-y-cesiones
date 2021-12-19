from mlib import cluster_0, cluster_1
import numpy as np
import pytest
from click.testing import CliRunner
from cli import predictcli


def test_cluster_0():
    data_to_predict = {
        'Monto activo':0,
        'Promedio Ventas': 0,
        'Promedio Cesiones': 0,
        'proyeccion ventas': 0,
        'proyeccion compras': 0
        }
    assert cluster_0(data_to_predict) == 0

def test_cluster_1():
    data_to_predict = {
        'Monto activo':0,
        'Promedio Ventas': 1,
        'Promedio Cesiones': 1,
        'proyeccion ventas': 0,
        'proyeccion compras': 0
        }
    assert cluster_1(data_to_predict) == 0

def test_cli_cluster_0():
    runner = CliRunner()
    result = runner.invoke(
        predictcli, 
        ["--monactivo", 0,
         "--meansales", 0,
         "--meancesiones", 0,
         "--proyecsales", 0,
         "--proyecbuys", 0]
        )
    assert result.exit_code == 0
    assert 'Cluster: 0' in result.output

def test_cli_cluster_1():
    runner = CliRunner()
    result = runner.invoke(
        predictcli, 
        ["--monactivo", 0,
         "--meansales", 1,
         "--meancesiones", 1,
         "--proyecsales", 0,
         "--proyecbuys", 0]
        )
    assert result.exit_code == 0
    assert 'Cluster: 1' in result.output

def test_cli_cluster_2():
    runner = CliRunner()
    result = runner.invoke(
        predictcli, 
        ["--monactivo", 0.0,
         "--meansales", 2.748703e+07,
         "--meancesiones", 2.186285e+07,
         "--proyecsales", 3510500.0,
         "--proyecbuys", 0.0]
        )
    assert result.exit_code == 0
    assert 'Cluster: 2' in result.output

def test_cli_cluster_3():
    runner = CliRunner()
    result = runner.invoke(
        predictcli, 
        ["--monactivo", 0.0,
         "--meansales", 1.311500e+10,
         "--meancesiones", 2.572712e+09,
         "--proyecsales", 3.101062e+09,
         "--proyecbuys", 3.047526e+09]
        )
    assert result.exit_code == 0
    assert 'Cluster: 3' in result.output

def test_cli_cluster_4():
    runner = CliRunner()
    result = runner.invoke(
        predictcli, 
        ["--monactivo", 272742288.0,
         "--meansales", 4.214773e+09,
         "--meancesiones", 2.882901e+09,
         "--proyecsales", 3.524934e+07,
         "--proyecbuys", 0.000000e+00]
        )
    assert result.exit_code == 0
    assert 'Cluster: 4' in result.output
