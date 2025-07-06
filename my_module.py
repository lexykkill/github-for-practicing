def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI)
    :param weight_kg: weight in kilograms
    :param height_m: height in meters
    :return: BMI value
    """
    return weight_kg / (height_m ** 2)


def calculate_average(scores):
    """
    Calculate average from a list of scores
    :param scores: list of numerical scores
    :return: average score
    """
    if not scores:
        return 0
    return sum(scores) / len(scores)


