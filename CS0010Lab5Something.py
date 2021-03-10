{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter your name:  Ste\n",
      "Please enter a number:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello Ste\n",
      "Hello Ste\n"
     ]
    }
   ],
   "source": [
    "name = input(\"Please enter your name: \")\n",
    "num = input(\"Please enter a number: \")\n",
    "i = 0\n",
    "try:\n",
    "    userInput = int(num)\n",
    "    while i < userInput:\n",
    "        print(\"Hello \" + name)\n",
    "        i = i + 1\n",
    "except:\n",
    "    print(\"Your number input must be an integer\")\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
