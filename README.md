# Python Simulation Crowd Intelligence
## crowdInt.py
The basic idea of the program is to simulate crowd intelligence by simulating guesses of a crowd dependent on their competence and plotting the results afterwards.<br><br>
The program starts with the following three prompts. First of all it will ask you for the correct answer of the question, that the crowd tries to guess.
Thereafter you can set the competence of the crowd, which ranges from 1 (least competent) to 10 (most competent). Finally you'll have to set the size of the crowd.<br><br> 
The program will use the correct answer and the competence factor to calculate the range of possible guesses. If the competence is set to 1, then the lowest possible guess will be
```lowest possible guess = correct answer - 100% * correct answer``` and the maximum ```highest possible guess = correct answer + 100% * correct answer```. 
If the competence is set to 2 it will be ```lowest possible guess = correct answer - 90% * correct answer``` and ```lowest possible guess = correct answer + 90% * correct answer```
The range of possible answers will become smaller and smaller until the competence of 10 where the lowest and highest possible guesses will be ```lowest possible guess = correct answer - 10% * correct answer```
and ```lowest possible guess = correct answer + 10% * correct answer```<br><br>Within this intervall the program will create a random guess for each crowd member.
Finally the average of all guesses is calculated and the results are plotted. The plot will contain all guesses (blue dots), the correct answer (green line) 
as well as the average of all guesses (red line). An example of such a plot is shown below. Here the correct answer was 85. 30 people were guessing and the competence was set to 5.<br><br>
![output](https://github.com/user-attachments/assets/5812dbd2-fbc6-4fe5-b646-1b32512a4a20)
## crowdIntGauss.py
In contrast to the ```crowdInt.py``` program this Python program uses the Gaussian model (normal distribution) instead of a crowd competence to simulate the guesses of the crowd. Instead of a crowd competence between one and ten you can set the standard deviation of the Gaussian model. Alternatively you can just hit Enter when asked to input the deviation to use the default standard deviation, which is the correct answer / 2. 
The following plot resulted from a simulation which had the correct answer of 100, used the default standard deviation (in this case 50) and collected the guesses of a crowd of 1000 people.<br><br>
![Screenshot from 2025-05-10 20-04-19](https://github.com/user-attachments/assets/96e8825b-0821-43e5-8f66-2d4d077f0746)
## Requirements
* Python3
* matplotlib : ```pip install matplotlib```
