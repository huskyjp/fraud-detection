import csv
import matplotlib.pyplot as plt
import random


def extract_election_vote_counts(file_name, column_name):

    """Calculate the vote counts for each of these contains data
    reported bt Iranian government. (contains in 2009 csv file).

    Arguments:
        file_name: csv file name
        column_name: list of column names

    Returns: a list of integers that contains the values in those
    columns from every row
     (the order of the integers does not matter).

     The Call: extract_election_vote_counts
     ("election-iran-2009.csv", ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"])
     Return: [1131111, 16920, 7246, 837858, 623946, 12199, 21609, 656508, ...

    ex.
    for row in input_file:
        print(row)

    {'age': '20', 'height': '62', 'id': '1', 'weight':
    '120.6', 'name': 'Alice'}
    {'age': '21', 'height': '74', 'id': '2', 'weight':
    '190.6', 'name': 'Freddie'}
    {'age': '17', 'height': '68', 'id': '3', 'weight':
    '120.0', 'name': 'Bob'}
    """
    # create new list that we will return
    new_list = []
    election_iran_2019_file = open(file_name)
    input_file = csv.DictReader(election_iran_2019_file)

    # read input file by nested for loop
    # we want values in those columns from every single row
    # then, replace "," to ""
    # Convert ut into int by casting since
    # the file is stored as string but we want
    # the value as integer. Finally, we will
    # append each value to the new list we created
    for row in input_file:
        for column in range(0, len(column_name)):
            this_column_val = row[(column_name[column])]

            if (len(this_column_val) > 0):
                replaced_this_column_val = this_column_val.replace(",", "")
                int_replaced_this_column_val = int(replaced_this_column_val)
                new_list.append(int_replaced_this_column_val)
    election_iran_2019_file.close()
    return new_list


def ones_and_tens_digit_histogram(numbers):
    """Produce an ouput a list of 10 numbers from a input list of numbers.

    Arguments:
        numbers: Lists of numbers

    Returns: In the returned list, the value at index i is the
    frequency with which digit i
    appeared in the ones place OR the tens place in the input list.
    (We are pooling together all the digits found in the ones places and
    the tens places in the input list.)

    The Call: ones_and_tens_digit_histogram([127, 426, 28, 9, 90])

    Return: [0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2]
             for j in new_two_num:
            tens_place = j / 10
            ones_place = j / 10
    """

    # Since pur parameter is lists of numbers, so we first convert those into
    # two digits and store in the temp_list.
    temp_list = []
    ones_list = []
    tens_list = []
    new_list = []
    for num in numbers:
        new_two_num = (num % 100)
        temp_list.append(new_two_num)

    # Now, temp_list contains only two degit integert so
    # devide that into ones and tens separatelly and store in each list
    # When we divide the integer by 10, we get only tens part, in contrast,
    # when we get remainder, we get only ones part.
    for num in temp_list:
        tens_place = (num // 10)
        ones_place = (num % 10)
        ones_list.append(ones_place)
        tens_list.append(tens_place)

    # new_list should contain float type
    # ratio of each number
    # frequency. We can use count function to count how many times
    # our current number is stored in the list. Then,
    # we can sum up those from each lists.
    # Since we want to get the ratio, we can
    # divide it by
    # length of both ones list and tens list.

    for i in range(0, 10):
        count_ones = ones_list.count(i)
        count_tens = tens_list.count(i)
        sum_ones_tens = count_ones + count_tens
        frequency_ratio = (float)((sum_ones_tens) / len((ones_list) + (
            tens_list)))

        new_list.append(frequency_ratio)

    return new_list


def plot_iranian_least_digits_histogram(histogram):
    ''' Graphs the frequencies of the ones and tens digits
    for the Iranian election data.
    Save your plot to a file named iran-digits.png using plt.savefig.
    Takes a histogram ""ones_and_tens_digit_histogram"".

    Arguments:
        histogram: A list of 10 numbers that indicates the frequency ratio.

    The call:
        plot_iranian_least_digits_histogram(histogram)

    Return: None (But, save as png and show)
    '''
    # We should expect the frequency should be all equal to 0.1
    # So, first draw horizontal line at 0.1 labeled Ideal.
    # List of length 10 will make the line.
    # User plt (pyplot is imported as plt)
    horizontal_line = [[0.1] for i in range(len(histogram))]
    plt.plot(horizontal_line, label="Ideal")
    plt.plot(histogram, label="Iran")
    plt.legend()
    plt.ylabel("frequency")
    plt.xlabel("Digit")
    plt.savefig("iran-digits.png")
    # plt.show()
    plt.savefig
    plt.clf()
    return None


# A number of samples we will use
def number_of_samples(new_list):
    """Count the number of samples we will use.
    Takes the list from  extract_election_vote_counts(file_name, column_name):
    and calculate the length of it.

    Arguments:
        new_list: A list of vote numbers from the specific file and
        candidate(s).

    The call:
        number_of_samples(new_list)

    Return: An integer of sample number
    """
    samples = len(new_list)
    return samples


# int to number_of_iranian_samples
# new random histogram depends on the sample size
def get_random_histogram(number_of_samples):
    """Generate new histogram depends on its
    length of sample number.

    Arguments:
        number_of_samples: An integer of sample number

    The call:
        get_random_histogram(number_of_samples)

    Return: A list of 10 numbers from an random input list of numbers
    from 0 to 99.
    """
    random_list = []
    for _ in range(number_of_samples):
        rand = random.randint(0, 99)
        random_list.append(rand)
        histogram = ones_and_tens_digit_histogram(random_list)

    return histogram


def plot_distribution_by_sample_size():
    """Creates five different collections (10, 50, 100, 1000, and 10,000)
    plus the ideal line. Random numbers is where every element in the
    collection is a different randome number 0<= x < 100.

    Argument: None

    Call:
        plot_distribution_by_sample_size()
    Return:
        None. (With new version of graph and save as random-digits.png)
    """
    # To avoide the plots will be drawn to the same window.
    plt.clf()
    # Create five different collections
    five_collection_list = [10, 50, 100, 1000, 10000]
    # horizontal line
    horizontal_line = [[0.1] for i in range(10)]
    plt.plot(horizontal_line, label="Ideal")

    # Generate random number for all new five collection list
    # by for loop.
    for size in five_collection_list:
        random_historgram = get_random_histogram(size)
        plt.plot(random_historgram, label=size)
    plt.legend()
    plt.xlabel('Digit')
    plt.ylabel('Frequency')
    plt.savefig('random-digits.png')
    # plt.show()
    plt.clf()

    return None


def mean_squared_error(numbers1, numbers2):
    """Computationally determine how similar (closer) two lines are.
    In one dataset, compute the difference between it and the corresponding
    point in the other dataset.(And √)
    The sum of the difference is divided by the
    length of the data set (list) to get the mean.

    Argument:
        numbers1: A list of numbers
        numbers2: A list of numbers
        * two lists are not same

    Call: mean_squared_error([1, 4, 9], [6, 5, 4])

    Return: 17.0 (The difference between two points.)
    """

    # Since both of parameter is the list,
    # we can loop with selecting its index
    # Get a sum of its absolute difference,
    # and divide it by its length to get
    # the average.
    sum = 0.0
    for i in range(len(numbers1)):
        diff = numbers1[i] - numbers2[i]
        sum += (diff)**2
    mse = sum / (float)(len(numbers1))
    return mse


def calculate_mse_with_uniform(histogram):
    """We will generate 10,000 samples of randomly
    generated data points and see how the election
    results compare to those 10,000 samples.

    Null hypothesis (H0) = Sample is not made up
    Alternative Hypothesis (H1) = Sample is made up

    Argument: histogram = ones_and_tens_digit_histogram

    Returns: A mean squared error of the given histogram with the
             uniform distribution. i. e. comparing the MSE between
             only[0.1...]list and random given list.

    Call: calculate_mse_with_uniform(histogram)

    Return: 0.000739583333335 (mean squared error of given histogram with
    the uniform distribution)
    """
    # Since we store ten list of integer in the histogram,
    # we can use that list of integer to create new list as unifrom_list
    # as [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], which is
    # horizontal line we created above.
    # Then, compare that list and our parameter of histogram to get
    # the mean squared error.

    uniformed_point = 0.1
    uniform_list = [uniformed_point for _ in histogram]

    mse_uniform = mean_squared_error(histogram, uniform_list)

    return mse_uniform


def compare_iranian_mse_to_samples(iranian_mse, number_of_iranian_samples):
    """Comapre two inputs, Iranian MSE and the number of data points in the Iranian
    dataset. Then, build 10,000 groups of random numbers, where
    each group is the same size
    as the Iranian election data.

    Arguments:
                iranian_mse: float integer calculated by
                calculate_mse_with_uniform(histogram)
                number_of_iranian_samples: The number of data points
                                           in the Iranian dataset

    Return: count_larger(iranian_mse, mse_compared_with_uniform_list)
            A number of larger mse

    Output: Print
            1. determine how many of the 10,000 random MSEs are larger than or
            equal to the Iran MSE (for our sample of the 2009
            Iranian election data, the MSE is ~0.0007)
            2. Determine how many of the 10,000 random MSEs
            aresmaller than the Iran MSE.

    Example: compare_iranian_mse_to_samples(0.000739583333333, 120)
            Quantity of MSEs larger than or equal to the
            2009 Iranian election MSE: ___
            Quantity of MSEs smaller than the 2009 Iranian election MSE: ___
            2009 Iranian election null hypothesis rejection level p: ___
    """

    # First we should get the random 120 list from random number
    # Use this function above when creating rondom 120 range list
    # Then, we make histogram by ones_and_tens_digit_histogram function

    # We will then compare this value with 0.1 uniformed histogram
    # by 10000 times.
    mse_compared_with_uniform_list = []
    for _ in range(10000):
        mse_compared_with_uniform = (calculate_mse_with_uniform(
            get_random_histogram(number_of_iranian_samples)))
        mse_compared_with_uniform_list.append(mse_compared_with_uniform)

    return count_larger(iranian_mse, mse_compared_with_uniform_list)


def count_larger(mses, mse_compared_with_uniform_list):
    """Compare two imputs, mses and mse from uniform list.
    uniform list is from compare_us_mse_to_samples(us_mse,
    number_of_us_samples).
    Determine how many of the 10,000 random MSEs are larger than or
    equal to the Iran MSE (for our sample of the 2009
    Iranian election data, the MSE is ~0.0007)
    2. Determine how many of the 10,000 random MSEs
    are smaller than the Iran MSE.

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

    # Since histogram is the list of random value, we should get different
    # float mse. So, find larger/lower list of value.
    # iranian_mse is around 0.0007
    larger_count_mse_final = 0
    for mse in mse_compared_with_uniform_list:
        if mse >= mses:
            larger_count_mse_final += 1

    return larger_count_mse_final


def final_iran_summary(iranian_mse, larger_count_mse_final):
    """Print out the iran summary of the required statement.

    Arguments:
        iranian_mse: Float integer calculated by
        calculate_mse_with_uniform(histogram)
        Larger_count_mse_final: A number of larger MSE
        calculated by'
        count_larger(mses, mse_compared_with_uniform_list)

    Call: final_iran_summary(iranian_mse, larger_count_mse_final)

    Return: None

    Print: Final result that required by the assignment
    """
    print("2009 Iranian election MSE: ", iranian_mse)
    print("Quantity of MSEs larger than or equal to the " +
          "2009 Iranian election MSE: ", larger_count_mse_final)
    print("Quantity of MSEs smaller than the " +
          "2009 Iranian election MSE: ", 10000 - larger_count_mse_final)
    print("2009 Iranian election null hypothesis rejection level p: ",
          (float)(larger_count_mse_final / 10000))


def final_us_summary(us_mse, larger_count_mse_final):
    """Print out the iran summary of the required statement.

    Arguments:
        us_mse: Float integer calculated by
        calculate_mse_with_uniform(histogram)
        Larger_count_mse_final: A number of larger MSE
        calculated by'
        count_larger(mses, mse_compared_with_uniform_list)

    Call: final_us_summary(us_mse, larger_count_mse_final)

    Return: None

    Print: Final result that required by the assignment
    """
    print("2008 United States election MSE:", us_mse)
    print("Quantity of MSEs larger than or equal to the " +
          "2008 United States election MSE: ", larger_count_mse_final)
    print("Quantity of MSEs smaller than the " +
          "2008 United States election MSE: ", 10000 - larger_count_mse_final)
    print("2008 United States election null hypothesis rejection level p: ",
          (float)(larger_count_mse_final / 10000))


def print_iranian_and_us_samples_mse_comparison():
    '''This function defines which candidates we wil look at.
    The function will be called in main function, therefore, there is
    no return in this function here.

    It will call 2 functions that are
    - final_iran_summary(iran_mse, count_larger(iran_mse,
                       compare_iranian_mse_to_samples
                       (iran_mse, iran_sample_number)))
    print()
    - final_us_summary(iran_mse, count_larger(iran_mse,
                     compare_us_mse_to_samples
                     (us_mse, us_sample_number)))
    '''

    # Define candidates we will use
    # for both iran and us
    iran_2009_candidates = ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"]
    us_2008_candidates = ["Obama", "McCain", "Nader", "Barr",
                          "Baldwin", "McKinney"]

    # By calling extract_election_vote_counts and
    # store a list of voting numbers
    vote_counts_iran_2009_election = extract_election_vote_counts(
        'election-iran-2009.csv', iran_2009_candidates)
    vote_counts_us_2008_election = extract_election_vote_counts(
        'election-us-2008.csv', us_2008_candidates)
    # By calling number_of_samples and
    # store a number of sample numbers we use
    iran_sample_number = number_of_samples(vote_counts_iran_2009_election)
    us_sample_number = number_of_samples(vote_counts_us_2008_election)

    # By calling ones_and_tens_digit_histogram and
    # get the frequency of the vote from the us/iran voting as
    # a list of
    iran_histogram = ones_and_tens_digit_histogram(
        vote_counts_iran_2009_election)
    us_histogram = ones_and_tens_digit_histogram(
        vote_counts_us_2008_election)

    # By calling calculate_mse_with_uniform and
    # get the squared error of given histogram with the
    # uniform distribution and store float number
    iran_mse = calculate_mse_with_uniform(iran_histogram)
    us_mse = calculate_mse_with_uniform(us_histogram)

    # By calling both compare_iranian_mse_to_samples and
    # compare_us_mse_to_samples by using "iran_mse",
    # "iran_sample_number", "us_mse", "us_sample_number"
    # which we just calculated within this function
    final_iran_summary(iran_mse, compare_iranian_mse_to_samples
                       (iran_mse, iran_sample_number))
    print()
    final_us_summary(us_mse, compare_iranian_mse_to_samples
                     (us_mse, us_sample_number))


# The code in this function is executed when
# this file is run as a Python program
def main():
    # Call function _iranian_and_us_samples_mse_comparison() which
    # also calls both final_iran_summary and
    # final_us_summary.
    print_iranian_and_us_samples_mse_comparison()


if __name__ == "__main__":
    main()
