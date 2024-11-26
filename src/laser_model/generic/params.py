"""
This module defines the function `get_parameters` which initializes and returns a `PropertySet` object containing
parameters for a measles simulation model. The parameters are divided into several categories: meta parameters,
measles-specific parameters, network parameters, and routine immunization (RI) parameters. The function also allows
for the optional loading of parameters from a JSON file and the overriding of parameters via command line arguments.

Functions:

    get_parameters(kwargs) -> PropertySet:

        Initializes and returns a `PropertySet` object with default parameters,
        optionally overridden by parameters from a JSON file and/or command line arguments.
"""

import re
from pathlib import Path

import click
from laser_core.propertyset import PropertySet


def get_parameters(kwargs) -> PropertySet:
    """
    Generate a set of parameters for the generic measles simulation.

    This function initializes default parameters for the simulation, including meta parameters,
    measles-specific parameters, network parameters, and routine immunization parameters. It then
    allows for these parameters to be overwritten by values from a JSON file and/or command line
    arguments.

    Args:

        kwargs (dict): A dictionary of keyword arguments that can include:

            - "params" (str): Path to a JSON file containing parameter values to overwrite defaults.
            - "param" (list): List of strings in the format "key=value" to overwrite specific parameters.

    Returns:

        PropertySet: A PropertySet object containing all the parameters for the simulation.
    """

    meta_params = PropertySet(
        {
            "nticks": 365,
            "verbose": False,
        }
    )

    params = PropertySet(meta_params)

    # Overwrite any default parameters with those from a JSON file (optional)
    if kwargs.get("params") is not None:
        paramfile = Path(kwargs.get("params"))
        params += PropertySet.load(paramfile)
        click.echo(f"Loaded parameters from `{paramfile}`…")

    # Finally, overwrite any parameters with those from the command line (optional)
    for key, value in kwargs.items():
        if key == "params":
            continue  # handled above

        if key != "param":
            click.echo(f"Using `{value}` for parameter `{key}` from the command line…")
            params[key] = value
        else:  # arbitrary param:value pairs from the command line
            for kvp in kwargs["param"]:
                key, value = re.split("[=:]+", kvp)
                if key not in params:
                    click.echo(f"Unknown parameter `{key}` ({value=}). Skipping…")
                    continue
                value = type(params[key])(value)  # Cast the value to the same type as the existing parameter
                click.echo(f"Using `{value}` for parameter `{key}` from the command line…")
                params[key] = value

    return params
