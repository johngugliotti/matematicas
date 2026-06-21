def generate_poly_title(coeffs):
    """Takes a list of coefficients [a_n, ..., a_1, a_0] and turns it into a

    beautiful LaTeX equation string for Matplotlib.
    """
    n = len(coeffs) - 1
    terms = []

    for i, c in enumerate(coeffs):
        power = n - i

        # 1. Skip terms where the coefficient is 0
        if c == 0:
            continue

        # 2. Handle the plus/minus sign between terms
        sign = ""
        if c > 0 and len(terms) > 0:
            sign = "+"
        elif c < 0:
            # If negative, the minus sign is naturally handled by str(c)
            pass

        # 3. Handle the coefficient text formatting
        if abs(c) == 1 and power > 0:
            # Hide the '1' for terms like x^2 or -x
            c_str = "-" if c < 0 else ""
        else:
            c_str = str(c)

        # 4. Handle the x variable and its exponent
        if power == 0:
            x_str = ""  # Constant term at the end
        elif power == 1:
            x_str = "x"  # Don't show x^1, just x
        else:
            x_str = f"x^{{{power}}}"  # Formats as x^n for LaTeX

        # Combine into a single term and add to our list
        terms.append(f"{sign}{c_str}{x_str}")

    # If all coefficients were 0, just return y = 0
    if not terms:
        return "$y = 0$"

    # Combine everything inside dollar signs $ for Matplotlib LaTeX styling
    equation_string = "".join(terms)
    return f"$y = {equation_string}$"                                                                                                                                                                                                    