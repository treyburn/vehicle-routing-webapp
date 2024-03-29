from random import randint
from tests.errors.errors import UnitTypeError, UnitValueError
from models.validate_inputs.generate_distance_matrix import _validate_inputs


def gen_dist_matrix(m_length: int, min_value: int, max_value: int,
                    asym: bool = False, asym_max: int = 1) -> list or None:
    """
        Generate random distance matrices based on user inputs in order to test Vehicle Routing Solver.
        This allows us to bypass the need for the (expensive) Distance Matrix API.

    :param m_length: number of distance matrix nodes
    :param min_value: minimum potential distance between nodes
    :param max_value: maximum potential distance between nodes
    :param asym: kwarg to indicate if reverse route is asymmetrical. (i.e. a -> b has a different length than b -> a).
        Set to False by default
    :param asym_max: kwarg to set maximum potential difference if routes between nodes are asymmetrical.
        Set to 1 by default.
    """

    try:
        _validate_inputs(m_length, min_value, max_value, asym, asym_max)
    except UnitTypeError or UnitValueError:
        return None

    dist_matrix = []

    # orig_node will represent each origin node position
    for orig_node in range(m_length):
        node_dist_list = []
        # dest_node represents the destination node position
        for dest_node in range(m_length):
            # If the destination node is the origin node then distance to itself is 0
            if dest_node == orig_node:
                node_dist_list.append(0)
            # If node pair has already been calculated, check if asymmetrical or not, and return appropriate result
            elif dest_node <= len(dist_matrix):
                # if asymmetrical - take previous distance and subtract random value between (-)asym_max and (+)asym_max
                # as long as that value is >= min_value - otherwise default to min_value
                if asym:
                    node_dist_list.append(max(
                                            dist_matrix[dest_node][orig_node] + randint(asym_max * -1, asym_max),
                                            min_value
                                          ))
                # if symmetrical - return previously calculated value
                else:
                    node_dist_list.append(dist_matrix[dest_node][orig_node])
            # If node pair hasn't been calculated yet - generate a random value within user specified constraints
            else:
                node_dist_list.append(randint(min_value, max_value))
        dist_matrix.append(node_dist_list)
    return dist_matrix
