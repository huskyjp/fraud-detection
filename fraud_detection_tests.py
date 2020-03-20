from fraud_detection import extract_election_vote_counts,\
    ones_and_tens_digit_histogram, number_of_samples,\
    mean_squared_error, calculate_mse_with_uniform,\
    count_larger


def test_extract_election_vote_counts():
    """ This test function checks if extract_election_vote_counts()
    works correctly or not by several possible examples.
    We use "Rezai" for iranian file, "Obama" for US file.

    Arguments:
        file_name: csv file name
        column_name: list of column names

    Returns: a list of integers that contains the values in those
    columns from every row
     (the order of the integers does not matter).
    """

    # set up
    # check iranian file using "Rezai"
    file_name = "election-iran-2009.csv"
    column_name = ["Rezai"]
    assert extract_election_vote_counts(file_name, column_name) \
        == [16920, 12199, 6578, 51788,
            5221, 7608, 147487, 22689,
            3962, 44809, 4129, 139124,
            7276, 4440, 6616, 23871,
            7978, 16297, 7140, 12016,
            11258, 8542, 5987, 12022,
            14920, 19587, 10057, 7237,
            13117, 8406]

    file_name = "election-us-2008.csv"
    column_name = ["Obama"]
    assert extract_election_vote_counts(file_name, column_name) \
        == [813479, 123594, 1034707, 422310,
            8274473, 1288576, 997772, 255459,
            245800, 4282074, 1844123, 325871,
            236440, 3419348, 1374039, 828940,
            514765, 751985, 782989, 232145,
            189778, 1629467, 1904097, 2872579,
            1573354, 554662, 1441911, 231667,
            121468, 138752, 73099, 533736,
            384826, 2215422, 472422, 4804701,
            2142651, 141278, 2940044, 502496,
            1037291, 3276363, 296571, 862449,
            170924, 1087437, 3528633, 327670,
            219262, 1959532, 1750848, 303857,
            1677211, 82868]
    print("Test extract election vote counts Passed!")


def test_ones_and_tens_digit_histogram():
    """This test function checks if ones_and_tens_digit_histogram()
    works correctly or not by several possible examples.

    We use 5 examples to test as below:
        1. [127, 426, 28, 9, 90]
        2. [0, 0, 0, 0, 0]
        3. [1, 0, 0, 0, 0]
        4. [1, 2, 3, 4, 5]
        5. [6, 7, 8, 9, 10]
    Arguments:
        numbers: Lists of numbers conatain 5 integer

    Returns: In the returned list, the value at index i is the
    frequency with which digit i
    appeared in the ones place OR the tens place in the input list.
    """
    assert ones_and_tens_digit_histogram([127, 426, 28, 9, 90]) \
        == [0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2]

    assert ones_and_tens_digit_histogram([0, 0, 0, 0, 0]) \
        == [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    assert ones_and_tens_digit_histogram([1, 0, 0, 0, 0]) \
        == [0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    assert ones_and_tens_digit_histogram([1, 2, 3, 4, 5]) \
        == [0.5, 0.1, 0.1, 0.1, 0.1, 0.1, 0.0, 0.0, 0.0, 0.0]

    assert ones_and_tens_digit_histogram([6, 7, 8, 9, 10]) \
        == [0.5, 0.1, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1]

    print("Test digit histogram passed!")


def test_number_of_samples():
    """ This test function checks if number_of_samples()
    works correctly or not by several possible examples.

    We use 3 examples to test as below:
    1.
    file_name = "election-iran-2009.csv"
    column_name = ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"]

    2.
    file_name = "election-us-2008.csv"
    column_name = ["Obama", "McCain", "Nader", "Barr", "Baldwin", "McKinney"]

    3.
    file_name = "election-us-2008.csv"
    column_name = ["Obama"]

    Arguments:
        new_list: A list of vote numbers from the specific file and
        candidate(s).

    The call:
        number_of_samples(new_list)

    Return: An integer of sample number
    """

    file_name = "election-iran-2009.csv"
    column_name = ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"]

    assert number_of_samples(extract_election_vote_counts(file_name,
                                                          column_name)) == 120

    file_name = "election-us-2008.csv"
    column_name = ["Obama", "McCain", "Nader", "Barr", "Baldwin", "McKinney"]
    assert number_of_samples(extract_election_vote_counts(file_name,
                                                          column_name)) == 302

    file_name = "election-us-2008.csv"
    column_name = ["Obama"]
    assert number_of_samples(extract_election_vote_counts(file_name,
                                                          column_name)) == 54
    print("Test number of samples passed!")


def test_mean_squared_error():
    """This test function checks if the difference between two points mean
    is correct or not by several possible examples.
    The sum of the difference is divided by the
    length of the data set (list) to get the mean.
        Argument:
         numbers1: A list of numbers
         numbers2: A list of numbers
         * two lists are not same

         Call: mean_squared_error([1, 4, 9], [6, 5, 4])

        Return: 17.0 (The difference between two points.)
    """

    numbers1 = [1, 4, 9]
    numbers2 = [6, 5, 4]
    assert mean_squared_error(numbers1, numbers2) == 17.0

    numbers1 = [1, 2, 3]
    numbers2 = [4, 5, 6]
    assert mean_squared_error(numbers1, numbers2) == 9.0

    numbers1 = [10, 20, 30]
    numbers2 = [40, 50, 60]
    assert mean_squared_error(numbers1, numbers2) == 900.0

    print("Test mean squared error passed!")


def test_calculate_mse_with_uniform():
    """This test function checks if the float value of comparison MSE between
    uniformed list and random given list is correct or not.

    We will generate 10,000 samples randomly
    generated data points and see how the election
    results compare to those 10,000 samples.

    We will use two examples as below:
    test_list = extract_election_vote_counts("election-iran-2009.csv",
                                             ["Ahmadinejad", "Rezai",
                                              "Karrubi", "Mousavi"])

    test_list = extract_election_vote_counts("election-us-2008.csv",
                                             ["Obama"])

    Argument: histogram = ones_and_tens_digit_histogram

    Returns: A mean squared error of the given histogram with the
             uniform distribution. i. e. comparing the MSE between
             only[0.1...]list and random given list.

    Call: calculate_mse_with_uniform(histogram)

    Return: 0.000739583333333 (mean squared error of given histogram with
    the uniform distribution)
    """

    test_list = extract_election_vote_counts("election-iran-2009.csv",
                                             ["Ahmadinejad", "Rezai",
                                              "Karrubi", "Mousavi"])
    freq_list_test = ones_and_tens_digit_histogram(test_list)
    assert calculate_mse_with_uniform(freq_list_test) == 0.0007395833333333335

    test_list = extract_election_vote_counts("election-us-2008.csv",
                                             ["Obama"])
    freq_list_test = ones_and_tens_digit_histogram(test_list)
    assert calculate_mse_with_uniform(freq_list_test) == 0.0006138545953360768

    print("Test calculate mse with uniform passed!")


def test_count_larger():
    """This test function checks if the funtion works correctly
    to produce a number of larger number which comapring between
    float integer from uniform and 10,000 random number histogram.

    Arguments:
                mse: float integer calculated by
                calculate_mse_with_uniform(histogram)
                mse_compared_with_uniform_list: List of mse
                 calculated from 10,000 groups of random numbers.

    Call:
        count_larger(mses, mse_compared_with_uniform_list)

    Return:
        larger_count_mse_final (A number of Larger integer than
        random mses)
    """
    mses = 0.7
    mse_compared_with_uniform_list = [0.1, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                      0.0, 0.0, 0.0]
    assert count_larger(mses, mse_compared_with_uniform_list) == 1

    mses = 0.01
    mse_compared_with_uniform_list = [0.01, 0.09, 0.9, 0.0, 0.0, 0.0, 0.0,
                                      0.0, 0.0, 0.0]
    assert count_larger(mses, mse_compared_with_uniform_list) == 3


if __name__ == '__main__':
    test_extract_election_vote_counts()
    test_ones_and_tens_digit_histogram()
    test_number_of_samples()
    test_mean_squared_error()
    test_calculate_mse_with_uniform()
    test_count_larger()
    print("All tests passed!!")
