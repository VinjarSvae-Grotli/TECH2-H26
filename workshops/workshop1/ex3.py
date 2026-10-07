import numpy as np


def tax(income):
    """
    Return the taxes owed for a given income.

    Parameters
    ----------
    income
        Gross income

    Returns
    -------
    Tax owed
    """
    if income <= 300_000:
        tax = 0
    elif income <= 700_000:
        tax = (income - 300_000) * 0.20
    else:
        tax = 400_000 * 0.20 + (income - 700_000) * 0.35

    return tax


print(tax(1_000_000))


def tax_sequence():
    """
    Return the taxes owed for a sequence of 13 incomes between 0 and 1,200,000.

    """
    incomes = np.linspace(0, 1_200_000, num=13)
    taxes_loop = np.empty_like(incomes)

    for i in range(len(incomes)):
        taxes_loop[i] = tax(incomes[i])

    after_tax = incomes - taxes_loop

    print(f"{'Income':>10} {'Tax':>10} {'After tax':>10}")
    for i in range(len(incomes)):
        print(f"{incomes[i]:10.0f} {taxes_loop[i]:10.0f} {after_tax[i]:10.0f}")

    return incomes, taxes_loop, after_tax

tax_sequence()

