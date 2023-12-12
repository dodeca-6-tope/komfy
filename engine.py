import importlib
import json


NODES_DIRECTORY = "nodes"


cache = {}


def is_node_ref(value):
    return value.startswith("$")


def run(workflow, output_node):
    args = workflow[output_node]["args"]

    if not any(is_node_ref(value) for value in args.values()):
        return run_node_caching(node_dict=workflow[output_node])

    for key, item in args.items():
        if is_node_ref(item):
            args[key] = run(workflow=workflow, output_node=item[1:])

    workflow[output_node]["args"] = args

    return run_node_caching(node_dict=workflow[output_node])


def run_node(node_dict):
    module = importlib.import_module(NODES_DIRECTORY + "." + node_dict["module"])

    return getattr(getattr(module, node_dict["node"]), "run")(**node_dict["args"])


def run_node_caching(node_dict):
    try:
        key = json.dumps(node_dict)

        if key not in cache:
            cache[key] = run_node(node_dict=node_dict)

        return cache[key]
    except:
        return run_node(node_dict=node_dict)
