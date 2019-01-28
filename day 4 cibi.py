{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "list=[1,2,3,4,5,6,7]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n"
     ]
    }
   ],
   "source": [
    "for i in list:\n",
    "    print(i)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# inline for loop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[x for x in range(1,11)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['c', 'i', 'b', 'i']"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[x for x in \"cibi\" ]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on NoneType object:\n",
      "\n",
      "class NoneType(object)\n",
      " |  Methods defined here:\n",
      " |  \n",
      " |  __bool__(self, /)\n",
      " |      self != 0\n",
      " |  \n",
      " |  __repr__(self, /)\n",
      " |      Return repr(self).\n",
      " |  \n",
      " |  ----------------------------------------------------------------------\n",
      " |  Static methods defined here:\n",
      " |  \n",
      " |  __new__(*args, **kwargs) from builtins.type\n",
      " |      Create and return a new object.  See help(type) for accurate signature.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(list.append(1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list.count(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4, 5, 6, 7, 1]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "list.reverse()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 7, 6, 5, 4, 3, 2, 1]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "dog\n",
      "4\n",
      "cat\n",
      "dog\n",
      "7\n",
      "8\n",
      "dog\n",
      "cat\n",
      "11\n",
      "dog\n",
      "13\n",
      "14\n",
      "dogcat\n",
      "16\n",
      "17\n",
      "dog\n",
      "19\n",
      "cat\n",
      "dog\n",
      "22\n",
      "23\n",
      "dog\n",
      "cat\n",
      "26\n",
      "dog\n",
      "28\n",
      "29\n",
      "dogcat\n",
      "31\n",
      "32\n",
      "dog\n",
      "34\n",
      "cat\n",
      "dog\n",
      "37\n",
      "38\n",
      "dog\n",
      "cat\n",
      "41\n",
      "dog\n",
      "43\n",
      "44\n",
      "dogcat\n",
      "46\n",
      "47\n",
      "dog\n",
      "49\n",
      "cat\n",
      "dog\n",
      "52\n",
      "53\n",
      "dog\n",
      "cat\n",
      "56\n",
      "dog\n",
      "58\n",
      "59\n",
      "dogcat\n",
      "61\n",
      "62\n",
      "dog\n",
      "64\n",
      "cat\n",
      "dog\n",
      "67\n",
      "68\n",
      "dog\n",
      "cat\n",
      "71\n",
      "dog\n",
      "73\n",
      "74\n",
      "dogcat\n",
      "76\n",
      "77\n",
      "dog\n",
      "79\n",
      "cat\n",
      "dog\n",
      "82\n",
      "83\n",
      "dog\n",
      "cat\n",
      "86\n",
      "dog\n",
      "88\n",
      "89\n",
      "dogcat\n",
      "91\n",
      "92\n",
      "dog\n",
      "94\n",
      "cat\n",
      "dog\n",
      "97\n",
      "98\n",
      "dog\n",
      "cat\n"
     ]
    }
   ],
   "source": [
    "#dog and cat\n",
    "for i in range(1,101):\n",
    "    if i%3==0 and i%5==0:\n",
    "         print(\"dogcat\")\n",
    "    elif i%3==0:\n",
    "        print(\"dog\")\n",
    "    elif i%5==0:\n",
    "        print(\"cat\")\n",
    "    else:\n",
    "        print(i)\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# funcitons"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "def run():\n",
    "    print(\"cibi\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "cibi\n"
     ]
    }
   ],
   "source": [
    "run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "def run(x,y):\n",
    "    z=x+y;\n",
    "    print(z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "run(1,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "def simple(agr):\n",
    "    num= 4+agr\n",
    "    return num"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "simple(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
