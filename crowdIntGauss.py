from random import uniform,gauss
import matplotlib.pyplot as plt

while True:
    print("Type '-1' to stop the program")
    try:
        # was is the correct solution?
        solution = float(input("What is the correct answer?: "))
        # stop program if input is '-1'
        if solution == -1:
            break
        # ask for standard deviation which is used in the gaussian model later
        stdDeviation = input("Which standard deviation should be used for the Gaussian model? (Hit Enter to use the default setting): ")
        stdDeviation = solution/2 if stdDeviation == "" else float(stdDeviation)
        # number of people partizipating
        crowdSize = int(input("How big is the audience?: "))

        guesses = list()
        persons = list()
        sumGuess = 0
        # each persons make his or her guess
        # guesses are saved to plot them later
        for i in range(crowdSize):
            guess = gauss(solution,stdDeviation)
            guesses.append(guess)
            persons.append(i+1)
            sumGuess += guess

        # calculation of average guess
        avg = round(sumGuess/crowdSize,2)
        print(f"The average guess was: {avg}")

        # necessary to plot the solution and average later
        solutions = list()
        avgs = list()
        for i in range(crowdSize):
            solutions.append(solution)
            avgs.append(avg)

        # scatter plot of all guesses
        plt.scatter(persons,guesses,color='blue')
        # plot of the solution as a green line
        plt.plot(persons,solutions,color='green')
        # plot of the average guess as a red line
        plt.plot(persons,avgs,color='red')
        plt.xlabel('Persons')
        plt.ylabel('Guesses')
        # showing average value in title
        plt.title(f"Average: {avg}")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")
        print("Please try again!")

    
    
