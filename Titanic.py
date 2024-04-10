{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e8ce5fb5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "import math "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "9ca07865",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C85</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>C123</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>male</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived  Pclass  \\\n",
       "0            1         0       3   \n",
       "1            2         1       1   \n",
       "2            3         1       3   \n",
       "3            4         1       1   \n",
       "4            5         0       3   \n",
       "\n",
       "                                                Name     Sex   Age  SibSp  \\\n",
       "0                            Braund, Mr. Owen Harris    male  22.0      1   \n",
       "1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
       "2                             Heikkinen, Miss. Laina  female  26.0      0   \n",
       "3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   \n",
       "4                           Allen, Mr. William Henry    male  35.0      0   \n",
       "\n",
       "   Parch            Ticket     Fare Cabin Embarked  \n",
       "0      0         A/5 21171   7.2500   NaN        S  \n",
       "1      0          PC 17599  71.2833   C85        C  \n",
       "2      0  STON/O2. 3101282   7.9250   NaN        S  \n",
       "3      0            113803  53.1000  C123        S  \n",
       "4      0            373450   8.0500   NaN        S  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic= pd.read_csv('train.csv')\n",
    "titanic.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0fb90479",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(891, 12)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a82ee525",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Survived', ylabel='count'>"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjsAAAGwCAYAAABPSaTdAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy88F64QAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAjZ0lEQVR4nO3de3BU9f3/8ddCyBJyWUkCu6wuiBpbNFFrsJD0q9xDKVdRQUkVR3TQKDUFjE2pigyTKI5AW0YsFg2CNE6rQR0tEq0EEZ3SFMrFu8YCJWu8hN0AcRPD+f3R8fy6BhSSTXb55PmY2Rn3nM+efR9nIM85e7I4LMuyBAAAYKhu0R4AAACgIxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADBaXLQHiAXHjh3TwYMHlZycLIfDEe1xAADASbAsSw0NDfJ6verW7cTXb4gdSQcPHpTP54v2GAAAoA3279+vs84664T7iR1JycnJkv77PyslJSXK0wAAgJMRDAbl8/nsn+MnQuxI9kdXKSkpxA4AAKeZ77sFhRuUAQCA0YgdAABgNGIHAAAYjdgBAABGI3YAAIDRiB0AAGA0YgcAABiN2AEAAEYjdgAAgNGIHQAAYDRiBwAAGI3YAQAARiN2AACA0YgdAABgNGIHAAAYLS7aA3Ql2Xc9Ge0RgJhT/dAN0R4BgOG4sgMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGhRjZ2FCxfK4XCEPTwej73fsiwtXLhQXq9XCQkJGj58uPbu3Rt2jFAopDlz5ig9PV2JiYmaNGmSDhw40NmnAgAAYlTUr+xceOGFqq2ttR+7d++29y1ZskRLly7VihUrtH37dnk8Ho0ZM0YNDQ32msLCQlVUVKi8vFxbt27V4cOHNWHCBLW0tETjdAAAQIyJi/oAcXFhV3O+YVmWli9frgULFmjq1KmSpDVr1sjtdmv9+vWaPXu2AoGAVq9erbVr12r06NGSpHXr1snn8+mVV17R2LFjj/ueoVBIoVDIfh4MBjvgzAAAQCyI+pWdDz74QF6vVwMHDtS1116rjz/+WJJUU1Mjv9+vvLw8e63T6dSwYcO0bds2SVJ1dbWam5vD1ni9XmVmZtprjqe0tFQul8t++Hy+Djo7AAAQbVGNnSFDhujJJ5/Uyy+/rMcee0x+v1+5ubn64osv5Pf7JUlutzvsNW63297n9/sVHx+v3r17n3DN8RQXFysQCNiP/fv3R/jMAABArIjqx1jjxo2z/zsrK0s5OTk699xztWbNGg0dOlSS5HA4wl5jWVarbd/2fWucTqecTmc7JgcAAKeLqH+M9b8SExOVlZWlDz74wL6P59tXaOrq6uyrPR6PR01NTaqvrz/hGgAA0LXFVOyEQiG988476tevnwYOHCiPx6PKykp7f1NTk6qqqpSbmytJys7OVo8ePcLW1NbWas+ePfYaAADQtUX1Y6z58+dr4sSJ6t+/v+rq6rR48WIFg0HNnDlTDodDhYWFKikpUUZGhjIyMlRSUqJevXppxowZkiSXy6VZs2Zp3rx5SktLU2pqqubPn6+srCz7t7MAAEDXFtXYOXDggK677jp9/vnn6tOnj4YOHaq33npLAwYMkCQVFRWpsbFRBQUFqq+v15AhQ7Rp0yYlJyfbx1i2bJni4uI0bdo0NTY2atSoUSorK1P37t2jdVoAACCGOCzLsqI9RLQFg0G5XC4FAgGlpKR02Ptk3/Vkhx0bOF1VP3RDtEcAcJo62Z/fMXXPDgAAQKQROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAo8VM7JSWlsrhcKiwsNDeZlmWFi5cKK/Xq4SEBA0fPlx79+4Ne10oFNKcOXOUnp6uxMRETZo0SQcOHOjk6QEAQKyKidjZvn27Vq1apYsuuihs+5IlS7R06VKtWLFC27dvl8fj0ZgxY9TQ0GCvKSwsVEVFhcrLy7V161YdPnxYEyZMUEtLS2efBgAAiEFRj53Dhw8rPz9fjz32mHr37m1vtyxLy5cv14IFCzR16lRlZmZqzZo1Onr0qNavXy9JCgQCWr16tR5++GGNHj1aP/rRj7Ru3Trt3r1br7zyygnfMxQKKRgMhj0AAICZoh47t99+u8aPH6/Ro0eHba+pqZHf71deXp69zel0atiwYdq2bZskqbq6Ws3NzWFrvF6vMjMz7TXHU1paKpfLZT98Pl+EzwoAAMSKqMZOeXm5/vnPf6q0tLTVPr/fL0lyu91h291ut73P7/crPj4+7IrQt9ccT3FxsQKBgP3Yv39/e08FAADEqLhovfH+/ft15513atOmTerZs+cJ1zkcjrDnlmW12vZt37fG6XTK6XSe2sAAAOC0FLUrO9XV1aqrq1N2drbi4uIUFxenqqoq/e53v1NcXJx9RefbV2jq6ursfR6PR01NTaqvrz/hGgAA0LVFLXZGjRql3bt3a+fOnfZj8ODBys/P186dO3XOOefI4/GosrLSfk1TU5OqqqqUm5srScrOzlaPHj3C1tTW1mrPnj32GgAA0LVF7WOs5ORkZWZmhm1LTExUWlqavb2wsFAlJSXKyMhQRkaGSkpK1KtXL82YMUOS5HK5NGvWLM2bN09paWlKTU3V/PnzlZWV1eqGZwAA0DVFLXZORlFRkRobG1VQUKD6+noNGTJEmzZtUnJysr1m2bJliouL07Rp09TY2KhRo0aprKxM3bt3j+LkAAAgVjgsy7KiPUS0BYNBuVwuBQIBpaSkdNj7ZN/1ZIcdGzhdVT90Q7RHAHCaOtmf31H/nh0AAICOROwAAACjETsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADAasQMAAIwWF+0BAMAE+xZlRXsEIOb0v3d3tEeQxJUdAABgOGIHAAAYjdgBAABGI3YAAIDRiB0AAGA0YgcAABiN2AEAAEYjdgAAgNGIHQAAYDRiBwAAGI3YAQAARiN2AACA0YgdAABgNGIHAAAYjdgBAABGI3YAAIDRiB0AAGC0NsXOyJEjdejQoVbbg8GgRo4c2d6ZAAAAIqZNsbN582Y1NTW12v7VV1/p9ddfb/dQAAAAkRJ3Kot37dpl//fbb78tv99vP29padHGjRt15plnRm46AACAdjql2LnkkkvkcDjkcDiO+3FVQkKCfv/730dsOAAAgPY6pdipqamRZVk655xz9Pe//119+vSx98XHx6tv377q3r17xIcEAABoq1OKnQEDBkiSjh071iHDAAAARFqbf/X8/fff16pVq7R48WItWrQo7HGyVq5cqYsuukgpKSlKSUlRTk6O/vrXv9r7LcvSwoUL5fV6lZCQoOHDh2vv3r1hxwiFQpozZ47S09OVmJioSZMm6cCBA209LQAAYJhTurLzjccee0y33Xab0tPT5fF45HA47H0Oh0P33nvvSR3nrLPO0gMPPKDzzjtPkrRmzRpNnjxZO3bs0IUXXqglS5Zo6dKlKisr0/nnn6/FixdrzJgxeu+995ScnCxJKiws1AsvvKDy8nKlpaVp3rx5mjBhgqqrq/lIDQAAyGFZlnWqLxowYIAKCgp09913R3yg1NRUPfTQQ7rpppvk9XpVWFhov08oFJLb7daDDz6o2bNnKxAIqE+fPlq7dq2mT58uSTp48KB8Pp9eeukljR079rjvEQqFFAqF7OfBYFA+n0+BQEApKSkRP6dvZN/1ZIcdGzhdVT90Q7RHiIh9i7KiPQIQc/rfu7tDjx8MBuVyub7353ebPsaqr6/XNddc0+bhjqelpUXl5eU6cuSIcnJyVFNTI7/fr7y8PHuN0+nUsGHDtG3bNklSdXW1mpubw9Z4vV5lZmbaa46ntLRULpfLfvh8voieCwAAiB1tip1rrrlGmzZtisgAu3fvVlJSkpxOp2699VZVVFToggsusL/Dx+12h613u932Pr/fr/j4ePXu3fuEa46nuLhYgUDAfuzfvz8i5wIAAGJPm+7ZOe+883TPPfforbfeUlZWlnr06BG2/xe/+MVJH+sHP/iBdu7cqUOHDumZZ57RzJkzVVVVZe//3/uBpP/etPztbd/2fWucTqecTudJzwgAAE5fbYqdVatWKSkpSVVVVWFhIv03Tk4lduLj4+0blAcPHqzt27frt7/9rX2fjt/vV79+/ez1dXV19tUej8ejpqYm1dfXh13dqaurU25ubltODQAAGKZNH2PV1NSc8PHxxx+3ayDLshQKhTRw4EB5PB5VVlba+5qamlRVVWWHTHZ2tnr06BG2pra2Vnv27CF2AACApDZe2YmUX//61xo3bpx8Pp8aGhpUXl6uzZs3a+PGjXI4HCosLFRJSYkyMjKUkZGhkpIS9erVSzNmzJAkuVwuzZo1S/PmzVNaWppSU1M1f/58ZWVlafTo0dE8NQAAECPaFDs33XTTd+5//PHHT+o4n376qa6//nrV1tbK5XLpoosu0saNGzVmzBhJUlFRkRobG1VQUKD6+noNGTJEmzZtsr9jR5KWLVumuLg4TZs2TY2NjRo1apTKysr4jh0AACCpjd+zc+WVV4Y9b25u1p49e3To0CGNHDlSzz77bMQG7Awn+3v67cX37ACt8T07gLli5Xt22nRlp6KiotW2Y8eOqaCgQOecc05bDgkAANAh2vxvY7U6ULdu+uUvf6lly5ZF6pAAAADtFrHYkaSPPvpIX3/9dSQPCQAA0C5t+hhr7ty5Yc8ty1Jtba1efPFFzZw5MyKDAQAAREKbYmfHjh1hz7t166Y+ffro4Ycf/t7f1AIAAOhMbYqd1157LdJzAAAAdIh2fangZ599pvfee08Oh0Pnn3+++vTpE6m5AAAAIqJNNygfOXJEN910k/r166crrrhCl19+ubxer2bNmqWjR49GekYAAIA2a1PszJ07V1VVVXrhhRd06NAhHTp0SM8995yqqqo0b968SM8IAADQZm36GOuZZ57RX/7yFw0fPtze9rOf/UwJCQmaNm2aVq5cGan5AAAA2qVNV3aOHj0qt9vdanvfvn35GAsAAMSUNsVOTk6O7rvvPn311Vf2tsbGRt1///3KycmJ2HAAAADt1aaPsZYvX65x48bprLPO0sUXXyyHw6GdO3fK6XRq06ZNkZ4RAACgzdoUO1lZWfrggw+0bt06vfvuu7IsS9dee63y8/OVkJAQ6RkBAADarE2xU1paKrfbrVtuuSVs++OPP67PPvtMd999d0SGAwAAaK823bPzhz/8QT/84Q9bbb/wwgv16KOPtnsoAACASGlT7Pj9fvXr16/V9j59+qi2trbdQwEAAERKm2LH5/PpjTfeaLX9jTfekNfrbfdQAAAAkdKme3ZuvvlmFRYWqrm5WSNHjpQkvfrqqyoqKuIblAEAQExpU+wUFRXpyy+/VEFBgZqamiRJPXv21N13363i4uKIDggAANAebYodh8OhBx98UPfcc4/eeecdJSQkKCMjQ06nM9LzAQAAtEubYucbSUlJuuyyyyI1CwAAQMS16QZlAACA0wWxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjRTV2SktLddlllyk5OVl9+/bVlClT9N5774WtsSxLCxculNfrVUJCgoYPH669e/eGrQmFQpozZ47S09OVmJioSZMm6cCBA515KgAAIEZFNXaqqqp0++2366233lJlZaW+/vpr5eXl6ciRI/aaJUuWaOnSpVqxYoW2b98uj8ejMWPGqKGhwV5TWFioiooKlZeXa+vWrTp8+LAmTJiglpaWaJwWAACIIXHRfPONGzeGPX/iiSfUt29fVVdX64orrpBlWVq+fLkWLFigqVOnSpLWrFkjt9ut9evXa/bs2QoEAlq9erXWrl2r0aNHS5LWrVsnn8+nV155RWPHjm31vqFQSKFQyH4eDAY78CwBAEA0xdQ9O4FAQJKUmpoqSaqpqZHf71deXp69xul0atiwYdq2bZskqbq6Ws3NzWFrvF6vMjMz7TXfVlpaKpfLZT98Pl9HnRIAAIiymIkdy7I0d+5c/d///Z8yMzMlSX6/X5LkdrvD1rrdbnuf3+9XfHy8evfufcI131ZcXKxAIGA/9u/fH+nTAQAAMSKqH2P9rzvuuEO7du3S1q1bW+1zOBxhzy3LarXt275rjdPplNPpbPuwAADgtBETV3bmzJmj559/Xq+99prOOusse7vH45GkVldo6urq7Ks9Ho9HTU1Nqq+vP+EaAADQdUU1dizL0h133KFnn31Wf/vb3zRw4MCw/QMHDpTH41FlZaW9rampSVVVVcrNzZUkZWdnq0ePHmFramtrtWfPHnsNAADouqL6Mdbtt9+u9evX67nnnlNycrJ9BcflcikhIUEOh0OFhYUqKSlRRkaGMjIyVFJSol69emnGjBn22lmzZmnevHlKS0tTamqq5s+fr6ysLPu3swAAQNcV1dhZuXKlJGn48OFh25944gndeOONkqSioiI1NjaqoKBA9fX1GjJkiDZt2qTk5GR7/bJlyxQXF6dp06apsbFRo0aNUllZmbp3795ZpwIAAGKUw7IsK9pDRFswGJTL5VIgEFBKSkqHvU/2XU922LGB01X1QzdEe4SI2LcoK9ojADGn/727O/T4J/vzOyZuUAYAAOgoxA4AADAasQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGhRjZ0tW7Zo4sSJ8nq9cjgc2rBhQ9h+y7K0cOFCeb1eJSQkaPjw4dq7d2/YmlAopDlz5ig9PV2JiYmaNGmSDhw40IlnAQAAYllUY+fIkSO6+OKLtWLFiuPuX7JkiZYuXaoVK1Zo+/bt8ng8GjNmjBoaGuw1hYWFqqioUHl5ubZu3arDhw9rwoQJamlp6azTAAAAMSwumm8+btw4jRs37rj7LMvS8uXLtWDBAk2dOlWStGbNGrndbq1fv16zZ89WIBDQ6tWrtXbtWo0ePVqStG7dOvl8Pr3yyisaO3Zsp50LAACITTF7z05NTY38fr/y8vLsbU6nU8OGDdO2bdskSdXV1Wpubg5b4/V6lZmZaa85nlAopGAwGPYAAABmitnY8fv9kiS32x223e122/v8fr/i4+PVu3fvE645ntLSUrlcLvvh8/kiPD0AAIgVMRs733A4HGHPLctqte3bvm9NcXGxAoGA/di/f39EZgUAALEnZmPH4/FIUqsrNHV1dfbVHo/Ho6amJtXX159wzfE4nU6lpKSEPQAAgJliNnYGDhwoj8ejyspKe1tTU5OqqqqUm5srScrOzlaPHj3C1tTW1mrPnj32GgAA0LVF9bexDh8+rA8//NB+XlNTo507dyo1NVX9+/dXYWGhSkpKlJGRoYyMDJWUlKhXr16aMWOGJMnlcmnWrFmaN2+e0tLSlJqaqvnz5ysrK8v+7SwAANC1RTV2/vGPf2jEiBH287lz50qSZs6cqbKyMhUVFamxsVEFBQWqr6/XkCFDtGnTJiUnJ9uvWbZsmeLi4jRt2jQ1NjZq1KhRKisrU/fu3Tv9fAAAQOxxWJZlRXuIaAsGg3K5XAoEAh16/072XU922LGB01X1QzdEe4SI2LcoK9ojADGn/727O/T4J/vzO2bv2QEAAIgEYgcAABiN2AEAAEYjdgAAgNGIHQAAYDRiBwAAGI3YAQAARiN2AACA0YgdAABgNGIHAAAYjdgBAABGI3YAAIDRiB0AAGA0YgcAABiN2AEAAEYjdgAAgNGIHQAAYDRiBwAAGI3YAQAARiN2AACA0YgdAABgNGIHAAAYjdgBAABGI3YAAIDRiB0AAGA0YgcAABiN2AEAAEYjdgAAgNGIHQAAYDRiBwAAGI3YAQAARiN2AACA0YgdAABgNGIHAAAYjdgBAABGI3YAAIDRiB0AAGA0YgcAABiN2AEAAEYjdgAAgNGIHQAAYDRiBwAAGI3YAQAARiN2AACA0YgdAABgNGIHAAAYjdgBAABGI3YAAIDRiB0AAGA0YgcAABiN2AEAAEYjdgAAgNGIHQAAYDRjYueRRx7RwIED1bNnT2VnZ+v111+P9kgAACAGGBE7Tz/9tAoLC7VgwQLt2LFDl19+ucaNG6d9+/ZFezQAABBlRsTO0qVLNWvWLN18880aNGiQli9fLp/Pp5UrV0Z7NAAAEGVx0R6gvZqamlRdXa1f/epXYdvz8vK0bdu2474mFAopFArZzwOBgCQpGAx23KCSWkKNHXp84HTU0X/uOkvDVy3RHgGIOR395/ub41uW9Z3rTvvY+fzzz9XS0iK32x223e12y+/3H/c1paWluv/++1tt9/l8HTIjgBNz/f7WaI8AoKOUujrlbRoaGuRynfi9TvvY+YbD4Qh7bllWq23fKC4u1ty5c+3nx44d05dffqm0tLQTvgbmCAaD8vl82r9/v1JSUqI9DoAI4s9312JZlhoaGuT1er9z3WkfO+np6erevXurqzh1dXWtrvZ8w+l0yul0hm0744wzOmpExKiUlBT+MgQMxZ/vruO7ruh847S/QTk+Pl7Z2dmqrKwM215ZWanc3NwoTQUAAGLFaX9lR5Lmzp2r66+/XoMHD1ZOTo5WrVqlffv26dZbuRcAAICuzojYmT59ur744gstWrRItbW1yszM1EsvvaQBAwZEezTEIKfTqfvuu6/VR5kATn/8+cbxOKzv+30tAACA09hpf88OAADAdyF2AACA0YgdAABgNGIHAAAYjdhBl/LII49o4MCB6tmzp7Kzs/X6669HeyQAEbBlyxZNnDhRXq9XDodDGzZsiPZIiCHEDrqMp59+WoWFhVqwYIF27Nihyy+/XOPGjdO+ffuiPRqAdjpy5IguvvhirVixItqjIAbxq+foMoYMGaJLL71UK1eutLcNGjRIU6ZMUWlpaRQnAxBJDodDFRUVmjJlSrRHQYzgyg66hKamJlVXVysvLy9se15enrZt2xalqQAAnYHYQZfw+eefq6WlpdU/Dut2u1v9I7IAALMQO+hSHA5H2HPLslptAwCYhdhBl5Cenq7u3bu3uopTV1fX6moPAMAsxA66hPj4eGVnZ6uysjJse2VlpXJzc6M0FQCgMxjxr54DJ2Pu3Lm6/vrrNXjwYOXk5GjVqlXat2+fbr311miPBqCdDh8+rA8//NB+XlNTo507dyo1NVX9+/eP4mSIBfzqObqURx55REuWLFFtba0yMzO1bNkyXXHFFdEeC0A7bd68WSNGjGi1febMmSorK+v8gRBTiB0AAGA07tkBAABGI3YAAIDRiB0AAGA0YgcAABiN2AEAAEYjdgAAgNGIHQAAYDRiBwAAGI3YAdAlbN68WQ6HQ4cOHerQ97nxxhs1ZcqUDn0PAKeG2AHQqerq6jR79mz1799fTqdTHo9HY8eO1Ztvvtmh75ubm6va2lq5XK4OfR8AsYd/CBRAp7rqqqvU3NysNWvW6JxzztGnn36qV199VV9++WWbjmdZllpaWhQX991/ncXHx8vj8bTpPQCc3riyA6DTHDp0SFu3btWDDz6oESNGaMCAAfrxj3+s4uJijR8/Xp988okcDod27twZ9hqHw6HNmzdL+v8fR7388ssaPHiwnE6nVq9eLYfDoXfffTfs/ZYuXaqzzz5blmWFfYwVCASUkJCgjRs3hq1/9tlnlZiYqMOHD0uS/vOf/2j69Onq3bu30tLSNHnyZH3yySf2+paWFs2dO1dnnHGG0tLSVFRUJP65QSD2EDsAOk1SUpKSkpK0YcMGhUKhdh2rqKhIpaWleuedd3T11VcrOztbTz31VNia9evXa8aMGXI4HGHbXS6Xxo8ff9z1kydPVlJSko4ePaoRI0YoKSlJW7Zs0datW5WUlKSf/vSnampqkiQ9/PDDevzxx7V69Wpt3bpVX375pSoqKtp1XgAij9gB0Gni4uJUVlamNWvW6IwzztBPfvIT/frXv9auXbtO+ViLFi3SmDFjdO655yotLU35+flav369vf/9999XdXW1fv7znx/39fn5+dqwYYOOHj0qSQoGg3rxxRft9eXl5erWrZv++Mc/KisrS4MGDdITTzyhffv22VeZli9fruLiYl111VUaNGiQHn30Ue4JAmIQsQOgU1111VU6ePCgnn/+eY0dO1abN2/WpZdeqrKyslM6zuDBg8OeX3vttfr3v/+tt956S5L01FNP6ZJLLtEFF1xw3NePHz9ecXFxev755yVJzzzzjJKTk5WXlydJqq6u1ocffqjk5GT7ilRqaqq++uorffTRRwoEAqqtrVVOTo59zLi4uFZzAYg+YgdAp+vZs6fGjBmje++9V9u2bdONN96o++67T926/fevpP+976W5ufm4x0hMTAx73q9fP40YMcK+uvOnP/3phFd1pP/esHz11Vfb69evX6/p06fbNzofO3ZM2dnZ2rlzZ9jj/fff14wZM9p+8gA6HbEDIOouuOACHTlyRH369JEk1dbW2vv+92bl75Ofn6+nn35ab775pj766CNde+2137t+48aN2rt3r1577TXl5+fb+y699FJ98MEH6tu3r84777ywh8vlksvlUr9+/ewrSZL09ddfq7q6+qTnBdA5iB0AneaLL77QyJEjtW7dOu3atUs1NTX685//rCVLlmjy5MlKSEjQ0KFD9cADD+jtt9/Wli1b9Jvf/Oakjz916lQFg0HddtttGjFihM4888zvXD9s2DC53W7l5+fr7LPP1tChQ+19+fn5Sk9P1+TJk/X666+rpqZGVVVVuvPOO3XgwAFJ0p133qkHHnhAFRUVevfdd1VQUNDhX1oI4NQROwA6TVJSkoYMGaJly5bpiiuuUGZmpu655x7dcsstWrFihSTp8ccfV3NzswYPHqw777xTixcvPunjp6SkaOLEifrXv/4VdpXmRBwOh6677rrjru/Vq5e2bNmi/v37a+rUqRo0aJBuuukmNTY2KiUlRZI0b9483XDDDbrxxhuVk5Oj5ORkXXnllafwfwRAZ3BYfCkEAAAwGFd2AACA0YgdAABgNGIHAAAYjdgBAABGI3YAAIDRiB0AAGA0YgcAABiN2AEAAEYjdgAAgNGIHQAAYDRiBwAAGO3/AW32dQN5linUAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x='Survived',data=titanic)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "68a0d682",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C85</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>C123</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>male</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>887</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>Montvila, Rev. Juozas</td>\n",
       "      <td>male</td>\n",
       "      <td>27.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>211536</td>\n",
       "      <td>13.0000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>888</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Graham, Miss. Margaret Edith</td>\n",
       "      <td>female</td>\n",
       "      <td>19.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>112053</td>\n",
       "      <td>30.0000</td>\n",
       "      <td>B42</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>889</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Johnston, Miss. Catherine Helen \"Carrie\"</td>\n",
       "      <td>female</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>W./C. 6607</td>\n",
       "      <td>23.4500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>890</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Behr, Mr. Karl Howell</td>\n",
       "      <td>male</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>111369</td>\n",
       "      <td>30.0000</td>\n",
       "      <td>C148</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>891</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Dooley, Mr. Patrick</td>\n",
       "      <td>male</td>\n",
       "      <td>32.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>370376</td>\n",
       "      <td>7.7500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Q</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>891 rows × 12 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     PassengerId  Survived  Pclass  \\\n",
       "0              1         0       3   \n",
       "1              2         1       1   \n",
       "2              3         1       3   \n",
       "3              4         1       1   \n",
       "4              5         0       3   \n",
       "..           ...       ...     ...   \n",
       "886          887         0       2   \n",
       "887          888         1       1   \n",
       "888          889         0       3   \n",
       "889          890         1       1   \n",
       "890          891         0       3   \n",
       "\n",
       "                                                  Name     Sex   Age  SibSp  \\\n",
       "0                              Braund, Mr. Owen Harris    male  22.0      1   \n",
       "1    Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
       "2                               Heikkinen, Miss. Laina  female  26.0      0   \n",
       "3         Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   \n",
       "4                             Allen, Mr. William Henry    male  35.0      0   \n",
       "..                                                 ...     ...   ...    ...   \n",
       "886                              Montvila, Rev. Juozas    male  27.0      0   \n",
       "887                       Graham, Miss. Margaret Edith  female  19.0      0   \n",
       "888           Johnston, Miss. Catherine Helen \"Carrie\"  female   NaN      1   \n",
       "889                              Behr, Mr. Karl Howell    male  26.0      0   \n",
       "890                                Dooley, Mr. Patrick    male  32.0      0   \n",
       "\n",
       "     Parch            Ticket     Fare Cabin Embarked  \n",
       "0        0         A/5 21171   7.2500   NaN        S  \n",
       "1        0          PC 17599  71.2833   C85        C  \n",
       "2        0  STON/O2. 3101282   7.9250   NaN        S  \n",
       "3        0            113803  53.1000  C123        S  \n",
       "4        0            373450   8.0500   NaN        S  \n",
       "..     ...               ...      ...   ...      ...  \n",
       "886      0            211536  13.0000   NaN        S  \n",
       "887      0            112053  30.0000   B42        S  \n",
       "888      2        W./C. 6607  23.4500   NaN        S  \n",
       "889      0            111369  30.0000  C148        C  \n",
       "890      0            370376   7.7500   NaN        Q  \n",
       "\n",
       "[891 rows x 12 columns]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "81bdd167",
   "metadata": {},
   "outputs": [],
   "source": [
    "#those who did not survived (more than 500 )are greater than who survived (nearly 300)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "0763ea28",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Survived', ylabel='count'>"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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TJQkxcXFKTc3V6tWrVL//v2b4QgvHLEDAICBevbs6fnvgIAARUREqEePHp5lTqdTklRSUiJJevrpp/WnP/1JX331lcrLy1VZWalrrrmmzn3v379fp0+fVlKS98XTlZWVuvbaaxv5SBqO2AEAwECtW7f2um+z2byW2Ww2SVJNTY2ef/55TZs2TU8++aQSExMVEhKiJ554Qn/961/r3HdNTY0k6dVXX9Vll13mtc5utzfmYTQKYgcAgBbunXfeUb9+/ZSamupZVlBQcNbtu3fvLrvdroMHD/rdS1Z1IXYAAGjhrrzySv33f/+33njjDcXGxmr9+vXatWuXYmNj69w+JCREM2fO1LRp01RTU6MbbrhBpaWlysvLU3BwsO69995mPoJzI3YAAGjhJk2apN27d2vs2LGy2Wy66667lJqa6nlrel1++9vfKioqShkZGfriiy8UFham3r17a86cOc04+YWxWZZl+XoIXystLZXD4ZDb7VZoaGiTPU9zfuImzo1PJAVwPqdPn1ZhYaFiY2PVtm1bX4/TYp3r3+FC/37zOTsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAACGsSxLv/71rxUeHi6bzabdu3f7ZI4vv/zSp89/Bt+NBQDARYpasaLZnqvkR99EfqG2bdumzMxMZWdnKy4uTpGRkU0w2aWD2AEAwDAFBQXq1KmT+vXr5+tR/AIvYwEAYJDx48drypQpOnjwoGw2m7p06SLLsrR48WLFxcUpKChIvXr10osvvuh5THZ2tmw2m9544w1de+21CgoK0qBBg1RSUqLXX39d3bp1U2hoqO666y6dOnXK87ht27bphhtuUFhYmCIiInTLLbeooKDgnPPt379fN998s4KDg+V0OnXPPffo22+/bbKfh0TsAABglKeeekqPPfaYOnfurKKiIu3atUvz5s3T2rVrtXLlSu3bt0/Tpk3T3XffrZycHK/HPvLII1q+fLny8vJ06NAhjRkzRsuWLdOmTZv06quvKisrS3/84x8925eVlWn69OnatWuX3nrrLbVq1Uq/+tWvVFNTU+dsRUVF6t+/v6655hp9+OGH2rZtm77++muNGTOmSX8mvIwFAIBBHA6HQkJCFBAQIJfLpbKyMi1ZskRvv/22EhMTJUlxcXHKzc3VqlWr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hs4EAADQaOoVO9nZ2aqsrKy1/PTp03rnnXcaPBQAAEBjCbyYjffs2eP57/3796u4uNhzv7q6Wtu2bdNll13WeNMBAAA00EXFzjXXXCObzSabzVbny1VBQUH64x//2GjDAQAANNRFxU5hYaEsy1JcXJw++OADdezY0bOuTZs2ioqKUkBAQKMPCQAAUF8XFTtXXHGFJKmmpqZJhgEAAGhsFxU7P3bgwAFlZ2erpKSkVvzMnz+/wYMBAAA0hnrFzrPPPqvJkycrMjJSLpdLNpvNs85msxE7AADAb9Qrdh5//HH97ne/0+zZsxt7HgAAgEZVr8/ZOXbsmO64447GngUAAKDR1St27rjjDm3fvr2xZwEAAGh09XoZ68orr9RDDz2k999/Xz169FDr1q291v/Hf/xHowwHAADQUDbLsqyLfVBsbOzZd2iz6YsvvmjQUM2ttLRUDodDbrdboaGhTfY8nVOymmzfuDiHNyb5egQAQANd6N/vep3ZKSwsrPdgAAAAzale1+wAAABcKup1ZmfChAnnXL9mzZp6DQMAANDY6hU7x44d87pfVVWlvXv36vjx43V+QSgAAICv1Ct2tmzZUmtZTU2NUlNTFRcX1+ChAAAAGkujXbPTqlUrTZs2TUuXLm2sXQIAADRYo16gXFBQoO+//74xdwkAANAg9XoZa/r06V73LctSUVGRXn31Vd17772NMhgAAEBjqFfsfPTRR173W7VqpY4dO+rJJ5887zu1AAAAmlO9YmfHjh2NPQcAAECTqFfsnPHNN9/os88+k81m01VXXaWOHTs21lwAAACNol4XKJeVlWnChAnq1KmTbrrpJt14442Kjo7WxIkTderUqcaeEQAAoN7qFTvTp09XTk6OXnnlFR0/flzHjx/XX/7yF+Xk5GjGjBmNPSMAAEC91etlrJdeekkvvviiBgwY4Fl28803KygoSGPGjNHKlSsbaz4AAC5K1IoVvh4B/1SSmurrESTV88zOqVOn5HQ6ay2PioriZSwAAOBX6hU7iYmJevjhh3X69GnPsvLycj366KNKTExstOEAAAAaql4vYy1btkzDhg1T586d1atXL9lsNu3evVt2u13bt29v7BkBAADqrV6x06NHD/3jH//Qhg0b9Omnn8qyLN15551KSUlRUFBQY88IAABQb/WKnYyMDDmdTt1///1ey9esWaNvvvlGs2fPbpThAAAAGqpe1+ysWrVKV199da3l//Iv/6Knn366wUMBAAA0lnrFTnFxsTp16lRreceOHVVUVNTgoQAAABpLvWInJiZG7777bq3l7777rqKjoxs8FAAAQGOp1zU79913n9LS0lRVVaVBgwZJkt566y3NmjWLT1AGAAB+pV6xM2vWLB09elSpqamqrKyUJLVt21azZ89Wenp6ow4IAADQEPWKHZvNpkWLFumhhx7SJ598oqCgIHXt2lV2u72x5wMAAGiQesXOGcHBwfrFL37RWLMAAAA0unpdoAwAAHCpIHYAAIDRiB0AAGA0YgcAABiN2AEAAEYjdgAAgNGIHQAAYDRiBwAAGI3YAQAARvNp7GRkZOgXv/iFQkJCFBUVpVGjRumzzz7z2sayLD3yyCOKjo5WUFCQBgwYoH379nltU1FRoSlTpigyMlLt27fXrbfeqsOHDzfnoQAAAD/l09jJycnRgw8+qPfff19ZWVn6/vvvlZycrLKyMs82ixcv1pIlS7R8+XLt2rVLLpdLSUlJOnHihGebtLQ0bdmyRZs3b1Zubq5OnjypW265RdXV1b44LAAA4Eca9N1YDbVt2zav+2vXrlVUVJTy8/N10003ybIsLVu2THPnztVtt90mSVq3bp2cTqc2bdqkBx54QG63W6tXr9b69es1ZMgQSdKGDRsUExOjN998U0OHDq31vBUVFaqoqPDcLy0tbcKjBAAAvuRX1+y43W5JUnh4uCSpsLBQxcXFSk5O9mxjt9vVv39/5eXlSZLy8/NVVVXltU10dLTi4+M92/xURkaGHA6H5xYTE9NUhwQAAHzMb2LHsixNnz5dN9xwg+Lj4yVJxcXFkiSn0+m1rdPp9KwrLi5WmzZt1KFDh7Nu81Pp6elyu92e26FDhxr7cAAAgJ/w6ctYP/ab3/xGe/bsUW5ubq11NpvN675lWbWW/dS5trHb7bLb7fUfFgAAXDL84szOlClT9PLLL2vHjh3q3LmzZ7nL5ZKkWmdoSkpKPGd7XC6XKisrdezYsbNuAwAAWi6fxo5lWfrNb36jP//5z3r77bcVGxvrtT42NlYul0tZWVmeZZWVlcrJyVG/fv0kSQkJCWrdurXXNkVFRdq7d69nGwAA0HL59GWsBx98UJs2bdJf/vIXhYSEeM7gOBwOBQUFyWazKS0tTQsWLFDXrl3VtWtXLViwQO3atdO4ceM8206cOFEzZsxQRESEwsPDNXPmTPXo0cPz7iwAANBy+TR2Vq5cKUkaMGCA1/K1a9dq/PjxkqRZs2apvLxcqampOnbsmPr27avt27crJCTEs/3SpUsVGBioMWPGqLy8XIMHD1ZmZqYCAgKa61AAAICfslmWZfl6CF8rLS2Vw+GQ2+1WaGhokz1P55Ss82+EZnF4Y5KvRwDQRKJWrPD1CPinktTUJt3/hf799osLlAEAAJoKsQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADBaoK8HAAATdE7J8vUIOON6Xw8Af8OZHQAAYDRiBwAAGM2nsbNz506NGDFC0dHRstls2rp1q9d6y7L0yCOPKDo6WkFBQRowYID27dvntU1FRYWmTJmiyMhItW/fXrfeeqsOHz7cjEcBAAD8mU9jp6ysTL169dLy5cvrXL948WItWbJEy5cv165du+RyuZSUlKQTJ054tklLS9OWLVu0efNm5ebm6uTJk7rllltUXV3dXIcBAAD8mE8vUB42bJiGDRtW5zrLsrRs2TLNnTtXt912myRp3bp1cjqd2rRpkx544AG53W6tXr1a69ev15AhQyRJGzZsUExMjN58800NHTq02Y4FAAD4J7+9ZqewsFDFxcVKTk72LLPb7erfv7/y8vIkSfn5+aqqqvLaJjo6WvHx8Z5t6lJRUaHS0lKvGwAAMJPfxk5xcbEkyel0ei13Op2edcXFxWrTpo06dOhw1m3qkpGRIYfD4bnFxMQ08vQAAMBf+G3snGGz2bzuW5ZVa9lPnW+b9PR0ud1uz+3QoUONMisAAPA/fhs7LpdLkmqdoSkpKfGc7XG5XKqsrNSxY8fOuk1d7Ha7QkNDvW4AAMBMfhs7sbGxcrlcysr6/08lraysVE5Ojvr16ydJSkhIUOvWrb22KSoq0t69ez3bAACAls2n78Y6efKkPv/8c8/9wsJC7d69W+Hh4br88suVlpamBQsWqGvXruratasWLFigdu3aady4cZIkh8OhiRMnasaMGYqIiFB4eLhmzpypHj16eN6dBQAAWjafxs6HH36ogQMHeu5Pnz5dknTvvfcqMzNTs2bNUnl5uVJTU3Xs2DH17dtX27dvV0hIiOcxS5cuVWBgoMaMGaPy8nINHjxYmZmZCggIaPbjAQAA/sdmWZbl6yF8rbS0VA6HQ263u0mv3+GLAv3H4Y1Jvh4BhuH3239UXv8PX4+AfypJTW3S/V/o32+/vWYHAACgMRA7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADCaTz9UEPCVqBUrfD0C/qmpP4cDADizAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADCaMbGzYsUKxcbGqm3btkpISNA777zj65EAAIAfMCJ2nnvuOaWlpWnu3Ln66KOPdOONN2rYsGE6ePCgr0cDAAA+ZkTsLFmyRBMnTtR9992nbt26admyZYqJidHKlSt9PRoAAPCxQF8P0FCVlZXKz8/Xf/7nf3otT05OVl5eXp2PqaioUEVFhee+2+2WJJWWljbdoJJqqsqadP+4cDXl5b4eAf/U1L93zYXfb//B77f/aOrf7zP7tyzrnNtd8rHz7bffqrq6Wk6n02u50+lUcXFxnY/JyMjQo48+Wmt5TExMk8wIP/SCrwfAGY6ZM309AkzD77ffaK7f7xMnTsjhcJx1/SUfO2fYbDav+5Zl1Vp2Rnp6uqZPn+65X1NTo6NHjyoiIuKsj4E5SktLFRMTo0OHDik0NNTX4wBoRPx+tyyWZenEiROKjo4+53aXfOxERkYqICCg1lmckpKSWmd7zrDb7bLb7V7LwsLCmmpE+KnQ0FD+ZwgYit/vluNcZ3TOuOQvUG7Tpo0SEhKUlZXltTwrK0v9+vXz0VQAAMBfXPJndiRp+vTpuueee9SnTx8lJibqmWee0cGDBzVp0iRfjwYAAHzMiNgZO3asvvvuOz322GMqKipSfHy8XnvtNV1xxRW+Hg1+yG636+GHH671UiaASx+/36iLzTrf+7UAAAAuYZf8NTsAAADnQuwAAACjETsAAMBoxA4AADAasYMWZcWKFYqNjVXbtm2VkJCgd955x9cjAWgEO3fu1IgRIxQdHS2bzaatW7f6eiT4EWIHLcZzzz2ntLQ0zZ07Vx999JFuvPFGDRs2TAcPHvT1aAAaqKysTL169dLy5ct9PQr8EG89R4vRt29f9e7dWytXrvQs69atm0aNGqWMjAwfTgagMdlsNm3ZskWjRo3y9SjwE5zZQYtQWVmp/Px8JScney1PTk5WXl6ej6YCADQHYgctwrfffqvq6upaXw7rdDprfYksAMAsxA5aFJvN5nXfsqxaywAAZiF20CJERkYqICCg1lmckpKSWmd7AABmIXbQIrRp00YJCQnKysryWp6VlaV+/fr5aCoAQHMw4lvPgQsxffp03XPPPerTp48SExP1zDPP6ODBg5o0aZKvRwPQQCdPntTnn3/uuV9YWKjdu3crPDxcl19+uQ8ngz/gredoUVasWKHFixerqKhI8fHxWrp0qW666SZfjwWggbKzszVw4MBay++9915lZmY2/0DwK8QOAAAwGtfsAAAAoxE7AADAaMQOAAAwGrEDAACMRuwAAACjETsAAMBoxA4AADAasQMAAIxG7ABoEbKzs2Wz2XT8+PEmfZ7x48dr1KhRTfocAC4OsQOgWZWUlOiBBx7Q5ZdfLrvdLpfLpaFDh+q9995r0uft16+fioqK5HA4mvR5APgfvggUQLMaPXq0qqqqtG7dOsXFxenrr7/WW2+9paNHj9Zrf5Zlqbq6WoGB5/7fWZs2beRyuer1HAAubZzZAdBsjh8/rtzcXC1atEgDBw7UFVdcoV/+8pdKT0/X8OHD9eWXX8pms2n37t1ej7HZbMrOzpb0/y9HvfHGG+rTp4/sdrtWr14tm82mTz/91Ov5lixZoi5dusiyLK+Xsdxut4KCgrRt2zav7f/85z+rffv2OnnypCTpf//3fzV27Fh16NBBERERGjlypL788kvP9tXV1Zo+fbrCwsIUERGhWbNmia8bBPwPsQOg2QQHBys4OFhbt25VRUVFg/Y1a9YsZWRk6JNPPtHtt9+uhIQEbdy40WubTZs2ady4cbLZbF7LHQ6Hhg8fXuf2I0eOVHBwsE6dOqWBAwcqODhYO3fuVG5uroKDg/Wv//qvqqyslCQ9+eSTWrNmjVavXq3c3FwdPXpUW7ZsadBxAWh8xA6AZhMYGKjMzEytW7dOYWFhuv766zVnzhzt2bPnovf12GOPKSkpST/72c8UERGhlJQUbdq0ybP+wIEDys/P1913313n41NSUrR161adOnVKklRaWqpXX33Vs/3mzZvVqlUr/elPf1KPHj3UrVs3rV27VgcPHvScZVq2bJnS09M1evRodevWTU8//TTXBAF+iNgB0KxGjx6tI0eO6OWXX9bQoUOVnZ2t3r17KzMz86L206dPH6/7d955p7766iu9//77kqSNGzfqmmuuUffu3et8/PDhwxUYGKiXX35ZkvTSSy8pJCREycnJkqT8/Hx9/vnnCgkJ8ZyRCg8P1+nTp1VQUCC3262ioiIlJiZ69hkYGFhrLgC+R+wAaHZt27ZVUlKS5s+fr7y8PI0fP14PP/ywWrX64X9JP77upaqqqs59tG/f3ut+p06dNHDgQM/Znf/5n/8561kd6YcLlm+//XbP9ps2bdLYsWM9FzrX1NQoISFBu3fv9rodOHBA48aNq//BA2h2xA4An+vevbvKysrUsWNHSVJRUZFn3Y8vVj6flJQUPffcc3rvvfdUUFCgO++887zbb9u2Tfv27dOOHTuUkpLiWde7d2/94x//UFRUlK688kqvm8PhkMPhUKdOnTxnkiTp+++/V35+/gXPC6B5EDsAms13332nQYMGacOGDdqzZ48KCwv1wgsvaPHixRo5cqSCgoJ03XXXaeHChdq/f7927typefPmXfD+b7vtNpWWlmry5MkaOHCgLrvssnNu379/fzmdTqWkpKhLly667rrrPOtSUlIUGRmpkSNH6p133lFhYaFycnI0depUHT58WJI0depULVy4UFu2bNGnn36q1NTUJv/QQgAXj9gB0GyCg4PVt29fLV26VDfddJPi4+P10EMP6f7779fy5cslSWvWrFFVVZX69OmjqVOn6vHHH7/g/YeGhmrEiBH6+9//7nWW5mxsNpvuuuuuOrdv166ddu7cqcsvv1y33XabunXrpgkTJqi8vFyhoaGSpBkzZujf/u3fNH78eCUmJiokJES/+tWvLuInAqA52Cw+FAIAABiMMzsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAwGrEDAACM9n9zCAxuWqRR4gAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x='Survived',hue='Sex',data=titanic ,palette='winter')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0d5450ea",
   "metadata": {},
   "outputs": [],
   "source": [
    "#analysis :0 represent not survived and 1 ius for siurvives \n",
    "#women are thrice more likely to survive than male"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "c7e183f5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Survived', ylabel='count'>"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjsAAAGwCAYAAABPSaTdAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy88F64QAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAvVklEQVR4nO3dfVRVdb7H8c+RhyMKHAWEc0gknLRrQjZhKU6p+IAx+ZSWNnq7ujJX5UMx6LJBZ4rmlqSzfJjJYibHxDQHb5OYc/M6UgZK5oyyYnzoybqYWhBlwBHEA9G+f7g8txM+InAO2/drrb0We+/f3r/vz7WQz/rt3z7HYhiGIQAAAJPq4O0CAAAAWhNhBwAAmBphBwAAmBphBwAAmBphBwAAmBphBwAAmBphBwAAmJq/twvwBd9//72+/PJLhYSEyGKxeLscAABwGQzD0KlTpxQdHa0OHS48f0PYkfTll18qJibG22UAAIBmOH78uLp3737B84QdSSEhIZLO/mOFhoZ6uRoAAHA5nE6nYmJi3H/HL4SwI7kfXYWGhhJ2AABoZy61BIUFygAAwNQIOwAAwNQIOwAAwNRYswMAQDvW2NiohoYGb5fRKgICAuTn53fV9yHsAADQDhmGofLyclVVVXm7lFbVpUsX2e32q/ocPMIOAADt0LmgExkZqU6dOpnuQ3ENw9Dp06dVUVEhSXI4HM2+F2EHAIB2prGx0R10wsPDvV1OqwkKCpIkVVRUKDIystmPtFigDABAO3NujU6nTp28XEnrOzfGq1mXRNgBAKCdMtujq/NpiTESdgAAgKkRdgAAgKkRdgAAQBPTp0/X+PHjvV1GiyDsAABgUtOnT5fFYpHFYlFAQIB69uyp+fPnq7a21tultSlePQcAwMTuuusurV27Vg0NDdq9e7ceeugh1dbWKjs729ultRlmdgAAMDGr1Sq73a6YmBhNmTJFU6dO1ZYtWyRJhw8f1t13363Q0FCFhITozjvv1GeffXbe+2zfvl133HGHunTpovDwcI0ePdqjbX19vebMmSOHw6GOHTvq+uuvV1ZWlvt8ZmamevToIavVqujoaD322GOtOu4fYmYH8JLrZq/2dgk+4YsXZnq7BOCaEhQUpIaGBn3xxRcaPHiwhg4dqp07dyo0NFTvvvuuvvvuu/NeV1tbq/T0dCUkJKi2tlZPPvmk7rnnHpWUlKhDhw76wx/+oK1bt+q//uu/1KNHDx0/flzHjx+XJP31r3/VihUrlJubq759+6q8vFz/+te/2mzMhB0AAK4R//znP7Vx40YNHz5cL7zwgmw2m3JzcxUQECBJ6t279wWvnThxosf+mjVrFBkZqQ8++EDx8fE6duyYevXqpTvuuEMWi0WxsbHutseOHZPdbteIESMUEBCgHj166Pbbb2+dQZ4Hj7EAADCx//7v/1ZwcLA6duyopKQkDR48WM8//7xKSkp05513uoPOpXz22WeaMmWKevbsqdDQUMXFxUk6G2Sks4uhS0pKdOONN+qxxx7Tjh073Nfed999qqurU8+ePTVz5kzl5eVdcAapNRB2AAAwseTkZJWUlOjjjz/WmTNntHnzZkVGRrq/d+pyjRkzRidPntTq1av1j3/8Q//4xz8knV2rI0m33nqrSktL9Z//+Z+qq6vTpEmTdO+990qSYmJi9PHHH+uFF15QUFCQZs2apcGDB1/VV0BcCcIOAAAm1rlzZ91www2KjY31mMW5+eabtXv37ssKHCdPntSHH36oX//61xo+fLj69OmjysrKJu1CQ0M1efJkrV69Wps2bdLrr7+ub7/9VtLZtUJjx47VH/7wBxUUFOi9997TwYMHW26gF8GaHQAArkFz5szR888/r/vvv18ZGRmy2Wzau3evbr/9dt14440ebbt27arw8HC99NJLcjgcOnbsmH71q195tFmxYoUcDoduueUWdejQQa+99prsdru6dOminJwcNTY2asCAAerUqZPWr1+voKAgj3U9rYmZHQAArkHh4eHauXOnampqNGTIECUmJmr16tXnXcPToUMH5ebmqri4WPHx8frlL3+p3/3udx5tgoODtWTJEvXv31+33Xabjh49qm3btqlDhw7q0qWLVq9erZ/97Ge6+eab9fbbb+tvf/ubwsPD22SsFsMwjDbpyYc5nU7ZbDZVV1crNDTU2+XgGsGr52fx6jlw5c6cOaPS0lLFxcWpY8eO3i6nVV1srJf795uZHQAAYGqEHQAAYGqEHQAAYGqEHQAAYGqEHQAAYGqEHQAAYGqEHQAAYGqEHQAAYGqEHQAAYGpe/W6s7OxsZWdn6+jRo5Kkvn376sknn1Rqaqqks18Xv27dOo9rBgwYoL1797r3XS6X5s+fr7/85S+qq6vT8OHD9eKLL6p79+5tNg4A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Rys+Pt7d5nxcLpecTqfHBgAAWt/ChQu1e/duHT16VAcPHtSiRYtUUFCgqVOntlqfXl+gfKFFSufCSlRUlEf7qKgoff7555Kk8vJyBQYGqmvXrk3alJeXX7DPrKwsPf300y08EgAAvK85H/TXlr766is98MADKisrk81m080336zt27dr5MiRrdan18POuUVKVVVVev311zVt2jQVFha6z1ssFo/2hmE0OfZjl2qTkZGh9PR0977T6VRMTEwzRwAAAC7XmjVr2rxPrz/GutAiJbvdLklNZmgqKircsz12u1319fWqrKy8YJvzsVqt7jfAzm0AAMCcvB52fuzcIqW4uDjZ7Xbl5+e7z9XX16uwsFCDBg2SJCUmJiogIMCjTVlZmQ4dOuRuAwAArm1efYy1cOFCpaamKiYmRqdOnVJubq4KCgq0fft2WSwWpaWlafHixerVq5d69eqlxYsXq1OnTpoyZYokyWazacaMGZo3b57Cw8MVFham+fPnKyEhQSNGjPDm0AAAgI/wati51CKlBQsWqK6uTrNmzVJlZaUGDBigHTt2KCQkxH2PFStWyN/fX5MmTVJdXZ2GDx+unJwc+fn5eWtYAADAh1gMwzC8XYS3OZ1O2Ww2VVdXs34Hbea62au9XYJP8PU3RwBfdObMGZWWlur6669XUFCQt8tpVXV1dTp69Kji4uLUsWNHj3OX+/fb59bsAACAiwsICJAknT592suVtL5zYzw35ubw+qvnAADgyvj5+alLly6qqKiQJHXq1OmSH8vS3hiGodOnT6uiokJdunS5quUphB0AANqhcx/Rci7wmFWXLl3cY20uwg4AAO2QxWKRw+FQZGSkGhoavF1OqwgICGiRF44IOwAAtGN+fn68gXwJLFAGAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACmRtgBAACm5tWwk5WVpdtuu00hISGKjIzU+PHj9fHHH3u0mT59uiwWi8c2cOBAjzYu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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x='Survived',hue='Pclass', data=titanic, palette='PuBu')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b36d329f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Analysis :the passenger who did not survived belong rthe 3 rd class\n",
    "#1st class passanger are more  likely to syurvive "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "09e889d8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: ylabel='Frequency'>"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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/fvVpUuXYJUJAABCSFBvY5WXl+vw4cPe86KiIu3evVtxcXGKi4vTlClT9PjjjysxMVHHjh3TK6+8ovj4ePXv31+SFBsbq+HDh2vcuHFq3Lix4uLiNH78eLVp08b77iwAAPDPLahhZ/v27crIyPCeX3mOJjs7W3PnztW+ffu0aNEinT9/XomJicrIyNDSpUsVHR3tfc2bb76pyMhIPfnkk/ryyy/Vs2dPLViwQBEREbe8HwAAEHocxhgT7CKCze12KzY2VmVlZTy/E8ZaTFwV7BL+KRybkRXsEgBA0nf//R1Wz+wAAADcKMIOAACwGmEHAABYjbADAACsRtgBAABWI+wAAACrEXYAAIDVCDsAAMBqhB0AAGA1wg4AALAaYQcAAFiNsAMAAKxG2AEAAFYj7AAAAKsRdgAAgNUIOwAAwGqEHQAAYDXCDgAAsBphBwAAWI2wAwAArEbYAQAAViPsAAAAqxF2AACA1Qg7AADAaoQdAABgNcIOAACwGmEHAABYjbADAACsRtgBAABWI+wAAACrEXYAAIDVCDsAAMBqhB0AAGA1wg4AALAaYQcAAFiNsAMAAKxG2AEAAFYj7AAAAKsRdgAAgNWCGnY2b96svn37KikpSQ6HQytWrPDOVVZWasKECWrTpo0aNmyopKQkDRkyRKdPn/a5Rvfu3eVwOHyOQYMG3eJOAABAqApq2Ll48aLatm2rOXPm1Ji7dOmSdu7cqddee007d+7UsmXLdOjQIT322GM11o4YMULFxcXeY968ebeifAAAEAYig/nDMzMzlZmZec252NhY5efn+4z953/+p+677z6dOHFCzZs39443aNBALperTmsFAADhKaye2SkrK5PD4dAdd9zhM75kyRLFx8erdevWGj9+vC5cuHDd63g8Hrndbp8DAADYKag7Ozfi8uXLmjhxop5++mnFxMR4xwcPHqzU1FS5XC7t379fkyZN0p49e2rsCn1TTk6Opk6deivKBgAAQRYWYaeyslKDBg1SdXW13n77bZ+5ESNGeP+clpamli1bKj09XTt37lT79u2veb1JkyZp7Nix3nO3263k5OS6KR4AAARVyIedyspKPfnkkyoqKtKGDRt8dnWupX379qpXr54KCwtrDTtOp1NOp7MuygUAACEmpMPOlaBTWFiogoICNW7c+Ftfc+DAAVVWVioxMfEWVAgAAEJd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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "titanic['Age'].plot.hist()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "f16e6cf8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#we notice that higest are group travellin  anre among the young age between 20-40\n",
    "#very few passsetnmnger inage group 70-80"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "12f90880",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: ylabel='Frequency'>"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA1IAAAGsCAYAAADXIZZHAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy88F64QAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAoyElEQVR4nO3df5DWdb3//8fGwgoEGz901x1QKdFGQaewTCo1+eGoqOmZUdPSkmY0lcMe4ZjmH9J8HECc0BqOZuWIP8box5FOM6aBaRQ5zkEUBWrKk6igu5FFyw9xF+H9/cPj9W0Fj7zXlWuB223mmul6v1977fOdrwHu897r2pqiKIoAAACw2z5Q7QEAAAD2NkIKAACgJCEFAABQkpACAAAoSUgBAACUJKQAAABKElIAAAAl1VZ7gJ5gx44deeWVVzJgwIDU1NRUexwAAKBKiqLIpk2b0tTUlA984J3vOwmpJK+88kqGDx9e7TEAAIAeYu3atRk2bNg7nhdSSQYMGJDkzf+zBg4cWOVpAACAatm4cWOGDx9eaYR3IqSSyo/zDRw4UEgBAADv+pYfHzYBAABQkpACAAAoSUgBAACUJKQAAABKElIAAAAlCSkAAICShBQAAEBJQgoAAKAkIQUAAFCSkAIAAChJSAEAAJQkpAAAAEoSUgAAACUJKQAAgJKEFAAAQElCCgAAoKTaag/Azg679sFqj1Dxwuwzqj0CAAD0OO5IAQAAlCSkAAAAShJSAAAAJQkpAACAkoQUAABASUIKAACgJCEFAABQkpACAAAoSUgBAACUJKQAAABKElIAAAAlCSkAAICShBQAAEBJQgoAAKAkIQUAAFCSkAIAAChJSAEAAJQkpAAAAEoSUgAAACUJKQAAgJKEFAAAQElCCgAAoCQhBQAAUJKQAgAAKElIAQAAlCSkAAAAShJSAAAAJQkpAACAkoQUAABASUIKAACgJCEFAABQkpACAAAoSUgBAACUJKQAAABKElIAAAAlVTWkZsyYkZqamk6PxsbGyvmiKDJjxow0NTWlb9++Ofnkk7N69epOr9He3p4pU6Zk6NCh6d+/f84666ysW7duT18KAACwH6n6Hamjjz46LS0tlcfKlSsr5+bMmZO5c+dm3rx5WbZsWRobGzNhwoRs2rSpsqa5uTkLFy7MggULsnTp0mzevDmTJk3K9u3bq3E5AADAfqC26gPU1na6C/WWoihy66235vrrr8+5556bJLn77rvT0NCQ+++/P5dddlna2tpy55135t5778348eOTJPfdd1+GDx+eRx55JKeeeuoevRYAAGD/UPU7Us8991yampoyYsSIXHDBBXn++eeTJGvWrElra2smTpxYWVtXV5eTTjopjz/+eJJk+fLl2bZtW6c1TU1NGTVqVGXNrrS3t2fjxo2dHgAAALurqiF1/PHH55577skvf/nLfP/7309ra2vGjh2bv/3tb2ltbU2SNDQ0dPqahoaGyrnW1tb06dMngwYNesc1uzJr1qzU19dXHsOHD+/mKwMAAPZlVQ2p0047Lf/yL/+S0aNHZ/z48XnwwQeTvPkjfG+pqanp9DVFUex07O3ebc11112Xtra2ymPt2rXv4SoAAID9TdV/tO+f9e/fP6NHj85zzz1Xed/U2+8srV+/vnKXqrGxMR0dHdmwYcM7rtmVurq6DBw4sNMDAABgd/WokGpvb88f/vCHHHzwwRkxYkQaGxuzePHiyvmOjo4sWbIkY8eOTZKMGTMmvXv37rSmpaUlq1atqqwBAADoblX91L7p06fnzDPPzCGHHJL169fnxhtvzMaNG3PJJZekpqYmzc3NmTlzZkaOHJmRI0dm5syZ6devXy688MIkSX19fSZPnpxp06ZlyJAhGTx4cKZPn175UUEAAID3Q1VDat26dfnCF76QV199NQceeGA+9alP5Yknnsihhx6aJLnmmmuydevWXHHFFdmwYUOOP/74LFq0KAMGDKi8xi233JLa2tqcd9552bp1a8aNG5f58+enV69e1bosAABgH1dTFEVR7SGqbePGjamvr09bW1uPeL/UYdc+WO0RKl6YfUa1RwAAgD1md9ugR71HCgAAYG8gpAAAAEoSUgAAACUJKQAAgJKEFAAAQElCCgAAoCQhBQAAUJKQAgAAKElIAQAAlCSkAAAAShJSAAAAJQkpAACAkoQUAABASUIKAACgJCEFAABQkpACAAAoSUgBAACUJKQAAABKElIAAAAlCSkAAICShBQAAEBJQgoAAKAkIQUAAFCSkAIAAChJSAEAAJQkpAAAAEoSUgAAACUJKQAAgJKEFAAAQElCCgAAoCQhBQAAUJKQAgAAKElIAQAAlCSkAAAAShJSAAAAJQkpAACAkoQUAABASUIKAACgJCEFAABQkpACAAAoSUgBAACUJKQAAABKElIAAAAlCSkAAICShBQAAEBJQgoAAKAkIQUAAFCSkAIAAChJSAEAAJQkpAAAAEoSUgAAACUJKQAAgJKEFAAAQElCCgAAoCQhBQAAUFKPCalZs2alpqYmzc3NlWNFUWTGjBlpampK3759c/LJJ2f16tWdvq69vT1TpkzJ0KFD079//5x11llZt27dHp4eAADYn/SIkFq2bFm+973v5Zhjjul0fM6cOZk7d27mzZuXZcuWpbGxMRMmTMimTZsqa5qbm7Nw4cIsWLAgS5cuzebNmzNp0qRs3759T18GAACwn6h6SG3evDkXXXRRvv/972fQoEGV40VR5NZbb83111+fc889N6NGjcrdd9+d1157Lffff3+SpK2tLXfeeWe+9a1vZfz48fnYxz6W++67LytXrswjjzzyjt+zvb09Gzdu7PQAAADYXVUPqSuvvDJnnHFGxo8f3+n4mjVr0tramokTJ1aO1dXV5aSTTsrjjz+eJFm+fHm2bdvWaU1TU1NGjRpVWbMrs2bNSn19feUxfPjwbr4qAABgX1bVkFqwYEGeeuqpzJo1a6dzra2tSZKGhoZOxxsaGirnWltb06dPn053st6+Zleuu+66tLW1VR5r1659r5cCAADsR2qr9Y3Xrl2bqVOnZtGiRTnggAPecV1NTU2n50VR7HTs7d5tTV1dXerq6soNDAAA8L+qdkdq+fLlWb9+fcaMGZPa2trU1tZmyZIl+c53vpPa2trKnai331lav3595VxjY2M6OjqyYcOGd1wDAADQ3aoWUuPGjcvKlSuzYsWKyuO4447LRRddlBUrVuTDH/5wGhsbs3jx4srXdHR0ZMmSJRk7dmySZMyYMendu3enNS0tLVm1alVlDQAAQHer2o/2DRgwIKNGjep0rH///hkyZEjleHNzc2bOnJmRI0dm5MiRmTlzZvr165cLL7wwSVJfX5/Jkydn2rRpGTJkSAYPHpzp06dn9OjRO314BQAAQHepWkjtjmuuuSZbt27NFVdckQ0bNuT444/PokWLMmDAgMqaW265JbW1tTnvvPOydevWjBs3LvPnz0+vXr2qODkAALAvqymKoqj2ENW2cePG1NfXp62tLQMHDqz2ODns2gerPULFC7PPqPYIAACwx+xuG1T990gBAADsbYQUAABASUIKAACgJCEFAABQkpACAAAoSUgBAACUJKQAAABKElIAAAAlCSkAAICShBQAAEBJQgoAAKAkIQUAAFCSkAIAAChJSAEAAJQkpAAAAEoSUgAAACUJKQAAgJKEFAAAQElCCgAAoCQhBQAAUJKQAgAAKElIAQAAlCSkAAAAShJSAAAAJQkpAACAkoQUAABASUIKAACgJCEFAABQUpdCas2aNd09BwAAwF6jSyF1+OGH53Of+1zuu+++vP766909EwAAQI/WpZB65pln8rGPfSzTpk1LY2NjLrvssvz3f/93d88GAADQI3UppEaNGpW5c+fm5Zdfzl133ZXW1tZ85jOfydFHH525c+fmr3/9a3fPCQAA0GO8pw+bqK2tzTnnnJMf//jHuemmm/LnP/8506dPz7Bhw3LxxRenpaWlu+YEAADoMd5TSD355JO54oorcvDBB2fu3LmZPn16/vznP+fRRx/Nyy+/nLPPPru75gQAAOgxarvyRXPnzs1dd92VP/7xjzn99NNzzz335PTTT88HPvBml40YMSJ33HFHPvrRj3brsAAAAD1Bl0Lq9ttvz6WXXpqvfOUraWxs3OWaQw45JHfeeed7Gg4AAKAn6lJIPffcc++6pk+fPrnkkku68vIAAAA9WpfeI3XXXXflJz/5yU7Hf/KTn+Tuu+9+z0MBAAD0ZF0KqdmzZ2fo0KE7HT/ooIMyc+bM9zwUAABAT9alkHrxxRczYsSInY4feuiheemll97zUAAAAD1Zl0LqoIMOyrPPPrvT8WeeeSZDhgx5z0MBAAD0ZF0KqQsuuCD/+q//msceeyzbt2/P9u3b8+ijj2bq1Km54IILuntGAACAHqVLn9p344035sUXX8y4ceNSW/vmS+zYsSMXX3yx90gBAAD7vC6FVJ8+ffKjH/0o/+///b8888wz6du3b0aPHp1DDz20u+cDAADocboUUm854ogjcsQRR3TXLAAAAHuFLoXU9u3bM3/+/PzqV7/K+vXrs2PHjk7nH3300W4ZDgAAoCfqUkhNnTo18+fPzxlnnJFRo0alpqamu+cCAADosboUUgsWLMiPf/zjnH766d09DwAAQI/XpY8/79OnTw4//PDungUAAGCv0KWQmjZtWr797W+nKIrungcAAKDH69KP9i1dujSPPfZYHnrooRx99NHp3bt3p/MPPPBAtwwHAADQE3UppD70oQ/lnHPO6e5ZAAAA9gpdCqm77rqru+cAAADYa3TpPVJJ8sYbb+SRRx7JHXfckU2bNiVJXnnllWzevLnbhgMAAOiJuhRSL774YkaPHp2zzz47V155Zf76178mSebMmZPp06fv9uvcfvvtOeaYYzJw4MAMHDgwJ5xwQh566KHK+aIoMmPGjDQ1NaVv3745+eSTs3r16k6v0d7enilTpmTo0KHp379/zjrrrKxbt64rlwUAALBbuhRSU6dOzXHHHZcNGzakb9++lePnnHNOfvWrX+326wwbNiyzZ8/Ok08+mSeffDKnnHJKzj777EoszZkzJ3Pnzs28efOybNmyNDY2ZsKECZU7YEnS3NychQsXZsGCBVm6dGk2b96cSZMmZfv27V25NAAAgHdVU3ThM8yHDh2a3/3udznyyCMzYMCAPPPMM/nwhz+cF154IUcddVRee+21Lg80ePDg3Hzzzbn00kvT1NSU5ubmfP3rX0/y5t2nhoaG3HTTTbnsssvS1taWAw88MPfee2/OP//8JG/+eOHw4cPzi1/8Iqeeeupufc+NGzemvr4+bW1tGThwYJdn7y6HXftgtUeoeGH2GdUeAQAA9pjdbYMu3ZHasWPHLu/4rFu3LgMGDOjKS2b79u1ZsGBBtmzZkhNOOCFr1qxJa2trJk6cWFlTV1eXk046KY8//niSZPny5dm2bVunNU1NTRk1alRlza60t7dn48aNnR4AAAC7q0shNWHChNx6662V5zU1Ndm8eXNuuOGGnH766aVea+XKlfngBz+Yurq6XH755Vm4cGGOOuqotLa2JkkaGho6rW9oaKica21tTZ8+fTJo0KB3XLMrs2bNSn19feUxfPjwUjMDAAD7ty6F1C233JIlS5bkqKOOyuuvv54LL7wwhx12WF5++eXcdNNNpV7ryCOPzIoVK/LEE0/ka1/7Wi655JL8/ve/r5yvqanptL4oip2Ovd27rbnuuuvS1tZWeaxdu7bUzAAAwP6tS79HqqmpKStWrMgPf/jDPPXUU9mxY0cmT56ciy66qNOHT+yOPn365PDDD0+SHHfccVm2bFm+/e1vV94X1dramoMPPriyfv369ZW7VI2Njeno6MiGDRs63ZVav359xo4d+47fs66uLnV1daXmBAAAeEuXf49U3759c+mll2bevHm57bbb8tWvfrV0RO1KURRpb2/PiBEj0tjYmMWLF1fOdXR0ZMmSJZVIGjNmTHr37t1pTUtLS1atWvV/hhQAAMB70aU7Uvfcc8//ef7iiy/erdf5xje+kdNOOy3Dhw/Ppk2bsmDBgvz617/Oww8/nJqamjQ3N2fmzJkZOXJkRo4cmZkzZ6Zfv3658MILkyT19fWZPHlypk2bliFDhmTw4MGZPn16Ro8enfHjx3fl0gAAAN5Vl0Jq6tSpnZ5v27Ytr732Wvr06ZN+/frtdkj95S9/yZe+9KW0tLSkvr4+xxxzTB5++OFMmDAhSXLNNddk69atueKKK7Jhw4Ycf/zxWbRoUadPBrzllltSW1ub8847L1u3bs24ceMyf/789OrVqyuXBgAA8K669HukduW5557L1772tfz7v//7bv/+pp7C75F6Z36PFAAA+5P39fdI7crIkSMze/bsne5WAQAA7Gu6LaSSpFevXnnllVe68yUBAAB6nC69R+rnP/95p+dFUaSlpSXz5s3Lpz/96W4ZDAAAoKfqUkh9/vOf7/S8pqYmBx54YE455ZR861vf6o65AAAAeqwuhdSOHTu6ew4AAIC9Rre+RwoAAGB/0KU7UldfffVur507d25XvgUAAECP1aWQevrpp/PUU0/ljTfeyJFHHpkk+dOf/pRevXrl4x//eGVdTU1N90wJAADQg3QppM4888wMGDAgd999dwYNGpQk2bBhQ77yla/ks5/9bKZNm9atQwIAAPQkXXqP1Le+9a3MmjWrElFJMmjQoNx4440+tQ8AANjndSmkNm7cmL/85S87HV+/fn02bdr0nocCAADoyboUUuecc06+8pWv5Kc//WnWrVuXdevW5ac//WkmT56cc889t7tnBAAA6FG69B6p7373u5k+fXq++MUvZtu2bW++UG1tJk+enJtvvrlbBwQAAOhpuhRS/fr1y2233Zabb745f/7zn1MURQ4//PD079+/u+cDAADocd7TL+RtaWlJS0tLjjjiiPTv3z9FUXTXXAAAAD1Wl0Lqb3/7W8aNG5cjjjgip59+elpaWpIkX/3qV330OQAAsM/rUkj927/9W3r37p2XXnop/fr1qxw///zz8/DDD3fbcAAAAD1Rl94jtWjRovzyl7/MsGHDOh0fOXJkXnzxxW4ZDAAAoKfq0h2pLVu2dLoT9ZZXX301dXV173koAACAnqxLIXXiiSfmnnvuqTyvqanJjh07cvPNN+dzn/tctw0HAADQE3XpR/tuvvnmnHzyyXnyySfT0dGRa665JqtXr87f//73/O53v+vuGQEAAHqULt2ROuqoo/Lss8/mk5/8ZCZMmJAtW7bk3HPPzdNPP52PfOQj3T0jAABAj1L6jtS2bdsyceLE3HHHHfnmN7/5fswEAADQo5W+I9W7d++sWrUqNTU178c8AAAAPV6XfrTv4osvzp133tndswAAAOwVuvRhEx0dHfnBD36QxYsX57jjjkv//v07nZ87d263DAcAANATlQqp559/PocddlhWrVqVj3/840mSP/3pT53W+JE/AABgX1cqpEaOHJmWlpY89thjSZLzzz8/3/nOd9LQ0PC+DAcAANATlXqPVFEUnZ4/9NBD2bJlS7cOBAAA0NN16cMm3vL2sAIAANgflAqpmpqand4D5T1RAADA/qbUe6SKosiXv/zl1NXVJUlef/31XH755Tt9at8DDzzQfRMCAAD0MKVC6pJLLun0/Itf/GK3DgMAALA3KBVSd9111/s1BwAAwF7jPX3YBAAAwP5ISAEAAJQkpAAAAEoSUgAAACUJKQAAgJKEFAAAQElCCgAAoCQhBQAAUJKQAgAAKElIAQAAlCSkAAAAShJSAAAAJQkpAACAkoQUAABASUIKAACgJCEFAABQkpACAAAoSUgBAACUJKQAAABKElIAAAAlVTWkZs2alU984hMZMGBADjrooHz+85/PH//4x05riqLIjBkz0tTUlL59++bkk0/O6tWrO61pb2/PlClTMnTo0PTv3z9nnXVW1q1btycvBQAA2I9UNaSWLFmSK6+8Mk888UQWL16cN954IxMnTsyWLVsqa+bMmZO5c+dm3rx5WbZsWRobGzNhwoRs2rSpsqa5uTkLFy7MggULsnTp0mzevDmTJk3K9u3bq3FZAADAPq6mKIqi2kO85a9//WsOOuigLFmyJCeeeGKKokhTU1Oam5vz9a9/Pcmbd58aGhpy00035bLLLktbW1sOPPDA3HvvvTn//POTJK+88kqGDx+eX/ziFzn11FPf9ftu3Lgx9fX1aWtry8CBA9/Xa9wdh137YLVHqHhh9hnVHgEAAPaY3W2DHvUeqba2tiTJ4MGDkyRr1qxJa2trJk6cWFlTV1eXk046KY8//niSZPny5dm2bVunNU1NTRk1alRlzdu1t7dn48aNnR4AAAC7q8eEVFEUufrqq/OZ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tz/eJKR6kB/96Edpbm7O9ddfn6effjqf/exnc9ppp+Wll16q9mjsAVu2bMmxxx6befPm7fL8nDlzMnfu3MybNy/Lli1LY2NjJkyYkE2bNlXWNDc3Z+HChVmwYEGWLl2azZs3Z9KkSdm+ffueugzeR0uWLMmVV16ZJ554IosXL84bb7yRiRMnZsuWLZU19sn+bdiwYZk9e3aefPLJPPnkkznllFNy9tlnV/6BY3/wdsuWLcv3vve9HHPMMZ2O2yscffTRaWlpqTxWrlxZOWd//K+CHuOTn/xkcfnll3c69tGPfrS49tprqzQR1ZKkWLhwYeX5jh07isbGxmL27NmVY6+//npRX19ffPe73y2Koij+8Y9/FL179y4WLFhQWfPyyy8XH/jAB4qHH354j83OnrN+/foiSbFkyZKiKOwTdm3QoEHFD37wA/uDnWzatKkYOXJksXjx4uKkk04qpk6dWhSFP0soihtuuKE49thjd3nO/vj/uSPVQ3R0dGT58uWZOHFip+MTJ07M448/XqWp6CnWrFmT1tbWTvujrq4uJ510UmV/LF++PNu2beu0pqmpKaNGjbKH9lFtbW1JksGDByexT+hs+/btWbBgQbZs2ZITTjjB/mAnV155Zc4444yMHz++03F7hSR57rnn0tTUlBEjRuSCCy7I888/n8T++Ge11R6AN7366qvZvn17GhoaOh1vaGhIa2trlaaip3hrD+xqf7z44ouVNX369MmgQYN2WmMP7XuKosjVV1+dz3zmMxk1alQS+4Q3rVy5MieccEJef/31fPCDH8zChQtz1FFHVf7xYn+QJAsWLMhTTz2VZcuW7XTOnyUcf/zxueeee3LEEUfkL3/5S2688caMHTs2q1evtj/+iZDqYWpqajo9L4pip2Psv7qyP+yhfdNVV12VZ599NkuXLt3pnH2yfzvyyCOzYsWK/OMf/8h//ud/5pJLLsmSJUsq5+0P1q5dm6lTp2bRokU54IAD3nGdvbL/Ou200yr/e/To0TnhhBPykY98JHfffXc+9alPJbE/Eh820WMMHTo0vXr12qnS169fv1Pxs/9565Ny/q/90djYmI6OjmzYsOEd17BvmDJlSn7+85/nsccey7BhwyrH7ROSpE+fPjn88MNz3HHHZdasWTn22GPz7W9/2/6gYvny5Vm/fn3GjBmT2tra1NbWZsmSJfnOd76T2trayn9re4W39O/fP6NHj85zzz3nz5J/IqR6iD59+mTMmDFZvHhxp+OLFy/O2LFjqzQVPcWIESPS2NjYaX90dHRkyZIllf0xZsyY9O7du9OalpaWrFq1yh7aRxRFkauuuioPPPBAHn300YwYMaLTefuEXSmKIu3t7fYHFePGjcvKlSuzYsWKyuO4447LRRddlBUrVuTDH/6wvUIn7e3t+cMf/pCDDz7YnyX/rBqfcMGuLViwoOjdu3dx5513Fr///e+L5ubmon///sULL7xQ7dHYAzZt2lQ8/fTTxdNPP10kKebOnVs8/fTTxYsvvlgURVHMnj27qK+vLx544IFi5cqVxRe+8IXi4IMPLjZu3Fh5jcsvv7wYNmxY8cgjjxRPPfVUccoppxTHHnts8cYbb1TrsuhGX/va14r6+vri17/+ddHS0lJ5vPbaa5U19sn+7brrrit+85vfFGvWrCmeffbZ4hvf+EbxgQ98oFi0aFFRFPYH7+yfP7WvKOyV/d20adOKX//618Xzzz9fPPHEE8WkSZOKAQMGVP5Nan+8SUj1MP/xH/9RHHrooUWfPn2Kj3/845WPNWbf99hjjxVJdnpccsklRVG8+XGjN9xwQ9HY2FjU1dUVJ554YrFy5cpOr7F169biqquuKgYPHlz07du3mDRpUvHSSy9V4Wp4P+xqfyQp7rrrrsoa+2T/dumll1b+DjnwwAOLcePGVSKqKOwP3tnbQ8pe2b+df/75xcEHH1z07t27aGpqKs4999xi9erVlfP2x5tqiqIoqnMvDAAAYO/kPVIAAAAlCSkAAICShBQAAEBJQgoAAKAkIQUAAFCSkAIAAChJSAEAAJQkpAAAAEoSUgAAACUJKQAAgJKEFAAAQEn/HyTv0YeLF9/xAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 1000x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "titanic['Fare'].plot.hist(bins=20,figsize=(10,5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "eb0ec8a6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#we observe that most opf the ticket bough5 aare under fare 100\n",
    "#and we few are on the higher side od fare i.e 220-500$ range "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "a153bb7b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='SibSp', ylabel='count'>"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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5X2cTqecTmfUvgsvvLCnRuySlJSUmPgPKRbx3HSO56ZzPDed47npHM/NqcXS8+JyuU67pte/QTkhIUE5OTmqqKiI2l9RUaH8/HybpgIAALGi11/ZkaRFixbpzjvv1JgxY5SXl6cNGzbok08+0d133233aAAAwGZGxM6MGTP0+eef66GHHlJ9fb2ysrL0yiuvaNiwYXaPdtacTqeWL1/e4WU28Nx8E56bzvHcdI7npnM8N6fWW58Xh2Wd7vNaAAAAvVevf88OAADANyF2AACA0YgdAABgNGIHAAAYjdiJMU899ZQyMjLUt29f5eTk6O2337Z7JNu99dZbuummm+T1euVwOLRt2za7R4oZxcXFGjt2rJKTkzVo0CDdcsst2rdvn91jxYT169dr1KhRkS8/y8vL06uvvmr3WDGnuLhYDodDfr/f7lFst2LFCjkcjqjN4/HYPVZM+Oqrr/Szn/1MGRkZSkxM1PDhw/XQQw/p+PHjdo92RoidGPLCCy/I7/frwQcf1O7du3XttddqypQp+uSTT+wezVZHjx7V6NGjVVJSYvcoMaeyslILFizQO++8o4qKCn311VcqKCjQ0aNH7R7NdkOGDNEjjzyiXbt2adeuXbr++ut18803q7a21u7RYkZVVZU2bNigUaNG2T1KzBg5cqTq6+sj2549e+weKSasWrVK//Vf/6WSkhJ9+OGHWr16tR599FE98cQTdo92RvjoeQzJzc3VVVddpfXr10f2jRgxQrfccouKi4ttnCx2OBwOlZWV6ZZbbrF7lJj02WefadCgQaqsrNR1111n9zgxJzU1VY8++qjmzp1r9yi2a25u1lVXXaWnnnpKK1eu1BVXXKF169bZPZatVqxYoW3btqmmpsbuUWLO1KlT5Xa79eyzz0b23XbbberXr582b95s42Rnhis7MaK1tVXV1dUqKCiI2l9QUKCdO3faNBV6m2AwKOnrX+r4/7W3t6u0tFRHjx5VXl6e3ePEhAULFujGG2/UxIkT7R4lpuzfv19er1cZGRmaOXOmDhw4YPdIMeGaa67RG2+8oY8++kiS9N5772nHjh264YYbbJ7szBjxDcom+Mc//qH29vYOf7zU7XZ3+COnwKlYlqVFixbpmmuuUVZWlt3jxIQ9e/YoLy9PX375pfr376+ysjJdfvnldo9lu9LSUr377ruqqqqye5SYkpub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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x='SibSp',data=titanic,palette='rocket')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "16b9cd46",
   "metadata": {},
   "outputs": [],
   "source": [
    "#we notice that most of the passanger do not have their siblings abrod"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "a875e352",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: ylabel='Frequency'>"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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dgAAgNEIOwAAwGiEHQAAYDRjws7atWuVk5Ojq666SgUFBXrnnXfsbgkAAMQBI8LOb3/7W/l8Pj311FP68MMPdfvtt2vs2LE6duyY3a0BAACbJdrdQCxUVVWprKxMjz76qCRp9erV2r59u9atW6fKykqbuwNgt4ELX7e7hZ+Ez5eOs7uFi9YT/zZ64nm2W48PO+3t7WpoaNDChQsjxktLS7Vnz57zviYUCikUCoXXA4GAJCkYDMa8v87QNzHfJ87vcvz7u9x64t8H5xkXwt/GldETz/PlcvZcWJb1g3U9Pux8+eWX6ujokNvtjhh3u93y+/3nfU1lZaWefvrpLuPZ2dmXpUdcGa7Vdnfw08B5xoXwt3FlcJ67amlpkcvluuD2Hh92znI4HBHrlmV1GTtr0aJFmjdvXni9s7NT//u//6usrKwLviYawWBQ2dnZOn78uDIyMmK2X1NxvrqPc9V9nKvu41x1H+eq+y7nubIsSy0tLfJ6vT9Y1+PDTu/evZWQkNBlFqepqanLbM9ZTqdTTqczYuyaa665XC0qIyOD/xguAuer+zhX3ce56j7OVfdxrrrvcp2rH5rROavH342VnJysgoIC1dbWRozX1taqqKjIpq4AAEC86PEzO5I0b948PfTQQyosLNTw4cO1fv16HTt2TDNnzrS7NQAAYDMjws7kyZP11Vdf6de//rUaGxuVl5enN954QwMGDLC1L6fTqV/96lddvjLD+XG+uo9z1X2cq+7jXHUf56r74uFcOawfu18LAACgB+vx1+wAAAD8EMIOAAAwGmEHAAAYjbADAACMRti5jNauXaucnBxdddVVKigo0DvvvGN3S3Hp7bff1t133y2v1yuHw6FXX33V7pbiUmVlpW699Valp6erb9++uvfee/XJJ5/Y3VbcWrdunW666abwg8yGDx+ubdu22d1W3KusrJTD4ZDP57O7lbi0ePFiORyOiMXj8djdVtw6efKkHnzwQWVlZSk1NVW33HKLGhoarngfhJ3L5Le//a18Pp+eeuopffjhh7r99ts1duxYHTt2zO7W4s7p06d18803a82aNXa3Etfq6uo0e/Zsvffee6qtrdV3332n0tJSnT592u7W4lL//v21dOlS7d27V3v37tVdd92le+65RwcPHrS7tbhVX1+v9evX66abbrK7lbg2ePBgNTY2hpf9+/fb3VJcam5u1ogRI5SUlKRt27bpL3/5i1auXHlZf7HgQrj1/DIZNmyYhg4dqnXr1oXHbrzxRt17772qrKy0sbP45nA4VFNTo3vvvdfuVuLeF198ob59+6qurk533HGH3e30CJmZmVqxYoXKysrsbiXutLa2aujQoVq7dq2WLFmiW265RatXr7a7rbizePFivfrqq9q3b5/drcS9hQsX6t13342LbzWY2bkM2tvb1dDQoNLS0ojx0tJS7dmzx6auYJpAICDp+w9w/LCOjg5VV1fr9OnTGj58uN3txKXZs2dr3LhxGj16tN2txL1Dhw7J6/UqJydHDzzwgA4fPmx3S3HptddeU2Fhoe6//3717dtXQ4YM0QsvvGBLL4Sdy+DLL79UR0dHlx8idbvdXX6wFIiGZVmaN2+ebrvtNuXl5dndTtzav3+/rr76ajmdTs2cOVM1NTUaNGiQ3W3Fnerqan3wwQfMOnfDsGHDtHnzZm3fvl0vvPCC/H6/ioqK9NVXX9ndWtw5fPiw1q1bp9zcXG3fvl0zZ87U448/rs2bN1/xXoz4uYh45XA4ItYty+oyBkTjscce08cff6zdu3fb3Upcu+GGG7Rv3z59/fXX+sMf/qBp06aprq6OwPP/OX78uObOnasdO3boqquusruduDd27NjwP+fn52v48OH62c9+phdffFHz5s2zsbP409nZqcLCQlVUVEiShgwZooMHD2rdunV6+OGHr2gvzOxcBr1791ZCQkKXWZympqYusz3AxZozZ45ee+017dq1S/3797e7nbiWnJys6667ToWFhaqsrNTNN9+sZ555xu624kpDQ4OamppUUFCgxMREJSYmqq6uTs8++6wSExPV0dFhd4txLS0tTfn5+Tp06JDdrcSdfv36dfkfixtvvNGWG3UIO5dBcnKyCgoKVFtbGzFeW1uroqIim7pCT2dZlh577DG98soreuutt5STk2N3Sz2OZVkKhUJ2txFXiouLtX//fu3bty+8FBYWaurUqdq3b58SEhLsbjGuhUIh/fWvf1W/fv3sbiXujBgxosvjMT799FNbfqSbr7Euk3nz5umhhx5SYWGhhg8frvXr1+vYsWOaOXOm3a3FndbWVv3tb38Lrx85ckT79u1TZmamrr32Whs7iy+zZ8/WSy+9pD/+8Y9KT08Pzxy6XC6lpKTY3F38+eUvf6mxY8cqOztbLS0tqq6u1p///Ge9+eabdrcWV9LT07tc95WWlqasrCyuBzuP8vJy3X333br22mvV1NSkJUuWKBgMatq0aXa3FneeeOIJFRUVqaKiQpMmTdL777+v9evXa/369Ve+GQuXzXPPPWcNGDDASk5OtoYOHWrV1dXZ3VJc2rVrlyWpyzJt2jS7W4sr5ztHkqyNGzfa3Vpcmj59evi/vz59+ljFxcXWjh077G6rRxg5cqQ1d+5cu9uIS5MnT7b69etnJSUlWV6v15o4caJ18OBBu9uKW//93/9t5eXlWU6n0/qnf/ona/369bb0wXN2AACA0bhmBwAAGI2wAwAAjEbYAQAARiPsAAAAoxF2AACA0Qg7AADAaIQdAABgNMIOAAAwGmEHAAAYjbADAACMRtgBAABGI+wAAACj/T9l60bI2bLN+QAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "titanic['Parch'].plot.hist()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "246dd3c2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Parch', ylabel='count'>"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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fHx86D02btyoqKgozZs3T52dncrJydH27dvPaw4AAGCuiPs9O3Y428/p83t2AACIPOf6e3bO68rO//aHP/xBu3fvVnNzs06dOhX23I9+9KOBvi0AAMCgGlDsbN26VQ888IBGjx4tj8cT9mPeDoeD2AEAABFjQLHz2GOP6fHHHw/9GQcAAIBINaDfs9PS0qI777xzsGcBAAAYdAOKnTvvvFOVlZWDPQsAAMCgG9DHWBMnTtSaNWu0f/9+paenKzo6Ouz573//+4MyHAAAwIUaUOxs2bJFI0eOVHV1taqrq8OeczgcxA4AAIgYA4qdhoaGwZ4DAADgohjQPTsAAABDxYCu7Nx7773f+PwvfvGLAQ0DAAAw2AYUOy0tLWGPu7u7dfjwYZ08ebLPPxAKAABglwHFTkVFRa99p06d0tKlS3X55Zdf8FAAAACDZdDu2bnsssv0gx/8QBs3bhystwQAALhgg3qD8n//93/r66+/Hsy3BAAAuCAD+hirsLAw7LFlWWpqatLrr7+uRYsWDcpgAAAAg2FAsfPBBx+EPb7sssuUnJysp5566qw/qQUAAHApDSh23n333cGeAwAA4KIYUOycduLECX300UdyOBy64oorlJycPFhzAQAADIoB3aDc0dGhe++9V2PHjtWNN96oadOmyev1Kj8/X19++eVgzwgAADBgA4qdwsJCVVdX67XXXtPJkyd18uRJvfLKK6qurtaKFSsGe0YAAIABG9DHWL/61a/0H//xH5oxY0Zo3/e+9z3FxsZq3rx5KisrG6z5AAAALsiArux8+eWXcrvdvfaPGTOGj7EAAEBEGVDsZGVl6ZFHHtFXX30V2tfZ2akf//jHysrKGrThAAAALtSAPsbatGmT8vLyNG7cOE2ZMkUOh0N1dXVyOp2qrKwc7BkBAAAGbECxk56ermPHjmnHjh36/e9/L8uydNddd2nhwoWKjY0d7BkBAAAGbECxU1paKrfbrX/+538O2/+LX/xCJ06c0MqVKwdlOAAAgAs1oHt2fv7zn+vKK6/stX/SpEn613/91wseCgAAYLAMKHb8fr/Gjh3ba39ycrKampoueCgAAIDBMqDY8fl8eu+993rtf++99+T1ei94KAAAgMEyoHt27rvvPhUUFKi7u1szZ86UJP36179WcXExv0EZAABElAHFTnFxsf785z9r6dKl6urqkiQN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OlqXX365ioqK1NHRYfdoAIYQ/hAogIj293//93ruuefU3d2tPXv26L777lNHR4fKysrO630sy1JPT4+iovifPeDbhis7ACKa0+mUx+ORz+fTggULtHDhQu3atUs7duxQZmam4uPj5fF4tGDBAjU3N4det3v3bjkcDr399tvKzMyU0+nUnj17dOrUKa1bt04TJ06U0+nU+PHj9fjjj4d9zY8//lg33XSTRowYoSlTpui//uu/LvVhAxhExA6AISU2Nlbd3d3q6urSo48+qg8//FC7du1SQ0ODFi9e3Gt9cXGxSktLdfToUU2ePFmrVq3SunXrtGbNGh05ckQ7d+6U2+0Oe83q1atVVFSkuro6XXHFFbr77rv19ddfX6IjBDDY+KvnACLW4sWLdfLkSe3atUuS9P777+t73/uecnJy9NJLL4Wtramp0d/+7d+qra1NI0eO1O7du3XTTTdp165duu222yRJbW1tSk5O1ubNm3Xffff1+nqffPKJUlJS9G//9m/Kz8+XJB05ckSTJk3S0aNHdeWVV17cAwZwUXBlB0BE+8///E+NHDlSw4cPV1ZWlm688UY988wz+uCDD3TbbbdpwoQJio+P14wZMyRJn376adjrMzMzQ/8+evSogsGgcnJyvvFrTp48OfTvsWPHSlLYR2QAhhZiB0BEu+mmm1RXV6ePPvpIX331lV5++WXFxcUpNzdXI0eO1I4dO1RTU6OKigpJUldXV9jr4+LiQv+OjY09p68ZHR0d+rfD4ZAknTp16kIPBYBNiB0AES0uLk4TJ07UhAkTQhHy+9//Xp9//rmeeOIJTZs2TVdeeeU5XXlJTU1VbGysfv3rX1/ssQFEEH4GE8CQM378eMXExOiZZ57RkiVLdPjwYT366KNnfd3w4cO1cuVKFRcXKyYmRjfccINOnDih+vr60D06AMzDlR0AQ05ycrK2b9+uf//3f9fVV1+tJ554Qj/5yU/O6bVr1qzRihUr9KMf/UhXXXWV5s+fz/04gOH4aSwAAGA0ruwAAACjETsAAMBoxA4AADAasQMAAIxG7AAAAKMROwAAwGjEDgAAMBqxAwAAjEbsAAAAoxE7AADAaMQOAAAw2v8F6pXPUQ36W8AAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x='Parch',data=titanic,palette='summer')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "11740ee4",
   "metadata": {},
   "outputs": [],
   "source": [
    "#data wrangling means cleanin the data removing the nulll values \n",
    "# dropinng unwanted "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "045e05fb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "PassengerId      0\n",
       "Survived         0\n",
       "Pclass           0\n",
       "Name             0\n",
       "Sex              0\n",
       "Age            177\n",
       "SibSp            0\n",
       "Parch            0\n",
       "Ticket           0\n",
       "Fare             0\n",
       "Cabin          687\n",
       "Embarked         2\n",
       "dtype: int64"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "7fb4e636",
   "metadata": {},
   "outputs": [],
   "source": [
    "#age and cabin has most null values and embark too has null valuesa \n",
    "# we can plot on it "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "db8450c6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(titanic.isnull(),cmap='spring')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "49b30080",
   "metadata": {},
   "outputs": [],
   "source": [
    "# here yellow colour is showuing the null vaklues highjt in c abin folloed age "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "254d3d9a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='Pclass', ylabel='Age'>"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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aB6v12s8Q6RQZgAArhcMBjVs2DDTMRylqKgoaq4mz2EmAADgakZHZnJzczVr1qwm6/x+v8rLyyUdGrKbNWuWnn32We3bt0/9+/fX008/rR49epiICwBwKK/Xq6KiIqMZgsGgRo0aJUlas2aNvF6v0TymHz+SjB9m6tGjh958883w7djY2PDPBQUFmjt3rpYuXapLLrlEjzzyiIYMGaKdO3cqPj7eRFwAgANZluWoQyper9dRedo644eZ2rVrp0AgEF7OO+88SYdGZebNm6eZM2dqzJgxSk9P17Jly3TgwAEVFhYaTg0AAJzCeJn529/+pqSkJKWmpurGG2/U3//+d0nSrl27VF5erqFDh4b39Xg8GjRokDZu3HjM+wuFQqqurm6yAACAtstomenfv7/+8Ic/qKioSIsWLVJ5ebkGDBigysrK8LwZv9/f5HeOnFNzNPn5+UpMTAwvycnJrfocAACAWUbLzPDhwzV27Fj17NlT11xzjf785z9LkpYtWxbe5/vfkbdt+7jfm58xY4aqqqrCS1lZWeuEBwAAjmB8AvCRzjrrLPXs2VN/+9vfNHr0aElSeXm5OnfuHN6noqKi2WjNkTwejzwez2nL5IQTMTnBka8Br8ch0XRCKgBwMkeVmVAopI8//lhXXHGFUlNTFQgEVFxcrN69e0uS6uvrVVJSotmzZ0csEydiau7wVw+jXTSdkAoAnMxomfnVr36lESNGqGvXrqqoqNAjjzyi6upqTZw4UZZlKScnR3l5eUpLS1NaWpry8vIUFxenrKwsk7EBAICDGC0ze/fu1U033aRvvvlG5513nn76059q8+bNSklJkSRNnz5ddXV1mjx5cvikeevWrTN2jpnay7KlGEcNZkWObUuNBw/9HNNOitbDK40HddZfV5hOAQA4gtFP5pUrVx53u2VZys3NVW5ubmQCnUhMOyn2DNMpDDrTdAAAAJoxfp4ZAACAU0GZAQAArkaZAQAArkaZAQAArkaZAQAArkaZAQAArkaZAQAArkaZAQAArkaZAQAArkaZAQAArkaZAQAArkaZAQAArkaZAQAArkaZAQAArkaZAQAArkaZAQAArkaZAQAArkaZAQAArkaZAQAArkaZAQAArkaZAQAArkaZAQAArkaZAQAArvaDy0x9fb127typgwcPns48AAAALdLiMnPgwAHdeuutiouLU48e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VZ83gNbByAwA43w+n7777jt9/vnnuvLKKzV48GC9/fbbSkhI0IYNG3Tw4MGj/l5tba2mTZumnj17qra2Vr/97W/1T//0T9q6datiYmL01FNPae3atfrjH/+orl27qqysTGVlZZKkl156SU888YRWrlypHj16qLy8XB988EEknzaA04QyA8Co//7v/1ZhYaGuvvpqPf3000pMTNTKlSt1xhlnSJIuueSSY/7u2LFjm9xevHixOnXqpB07dig9PV179uxRWlqaBg4cKMuylJKSEt53z549CgQCuuaaa3TGGWeoa9eu6tevX+s8SQCtisNMACLuT3/6k9q3by+v16uMjAxdeeWVmj9/vrZu3aorrrgiXGRO5LPPPlNWVpYuvPBCJSQkKDU1VdKhoiIdmmy8detWdevWTffcc4/WrVsX/t1x48aprq5OF154oX75y19q1apVxxwBAuBslBkAEXfVVVdp69at2rlzp4LBoF555RV16tRJPp+vRfczYsQIVVZWatGiRfrLX/6iv/zlL5IOzZWRpMsuu0y7du3Sww8/rLq6Ot1www26/vrrJUnJycnauXOnnn76afl8Pk2ePFlXXnmlvvvuu9P7ZAG0OsoMgIg766yzdPHFFyslJaXJKEyvXr307rvvnlShqKys1Mcff6xf//rXuvrqq/WjH/1I+/bta7ZfQkKCxo8fr0WLFumFF17Qyy+/rP/3//6fpENzdUaOHKmnnnpK69ev16ZNm7Rt27bT90QBRARzZgA4xl133aX58+frxhtv1IwZM5SYmKjNmzerX79+6tatW5N9zz77bHXs2FHPPvusOnfurD179uj+++9vss8TTzyhzp076yc/+YliYmL04osvKhAIqEOHDlq6dKkaGhrUv39/xcXF6fnnn5fP52syrwaAOzAyA8AxOnbsqLffflv79+/XoEGDdPnll2vRokVHnUMTExOjlStX6v3331d6erqmTp2qxx9/vMk+7du31+zZs9WnTx/17dtX//u//6vXXntNMTEx6tChgxYtWqTMzEz16tVLb731ll599VV17NgxUk8XwGli2bZtmw4BAADwQzEyAwAAXI0yAwAAXI0yAwAAXI0yAwAAXI0yAwAAXI0yAwAAXI0yAwAAXI0yAwAAXI0yAwAAXI0yAwAAXI0yAwAAXO3/A/Iah8W53fsCAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(x='Pclass',y='Age',data=titanic)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "5ba14795",
   "metadata": {},
   "outputs": [],
   "source": [
    "#we can observe that older agegroup are travling more in class 1 and 2\n",
    "# comapared to class 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "eaa47892",
   "metadata": {},
   "outputs": [],
   "source": [
    "# the hue parameter determines which colums in the datya frame should be used for colour encoding "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "6a9e8713",
   "metadata": {},
   "outputs": [],
   "source": [
    "#we will drop a frew coloums and  row "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "840fab1b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C85</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>C123</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>male</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived  Pclass  \\\n",
       "0            1         0       3   \n",
       "1            2         1       1   \n",
       "2            3         1       3   \n",
       "3            4         1       1   \n",
       "4            5         0       3   \n",
       "\n",
       "                                                Name     Sex   Age  SibSp  \\\n",
       "0                            Braund, Mr. Owen Harris    male  22.0      1   \n",
       "1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
       "2                             Heikkinen, Miss. Laina  female  26.0      0   \n",
       "3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   \n",
       "4                           Allen, Mr. William Henry    male  35.0      0   \n",
       "\n",
       "   Parch            Ticket     Fare Cabin Embarked  \n",
       "0      0         A/5 21171   7.2500   NaN        S  \n",
       "1      0          PC 17599  71.2833   C85        C  \n",
       "2      0  STON/O2. 3101282   7.9250   NaN        S  \n",
       "3      0            113803  53.1000  C123        S  \n",
       "4      0            373450   8.0500   NaN        S  "
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "5decfbab",
   "metadata": {},
   "outputs": [],
   "source": [
    "#droping the "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "615cd367",
   "metadata": {},
   "outputs": [],
   "source": [
    "titanic.drop('Cabin',axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "a7a079bb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived  Pclass  \\\n",
       "0            1         0       3   \n",
       "1            2         1       1   \n",
       "2            3         1       3   \n",
       "\n",
       "                                                Name     Sex   Age  SibSp  \\\n",
       "0                            Braund, Mr. Owen Harris    male  22.0      1   \n",
       "1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
       "2                             Heikkinen, Miss. Laina  female  26.0      0   \n",
       "\n",
       "   Parch            Ticket     Fare Embarked  \n",
       "0      0         A/5 21171   7.2500        S  \n",
       "1      0          PC 17599  71.2833        C  \n",
       "2      0  STON/O2. 3101282   7.9250        S  "
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "27f84c6d",
   "metadata": {},
   "outputs": [],
   "source": [
    "titanic.dropna(inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "2d575159",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAigAAAHqCAYAAAAuxbWnAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy88F64QAAAACXBIWXMAAA9hAAAPYQGoP6dpAABt3UlEQVR4nO3deVyNef8/8NdpO+2lvUybmFChcFtnhESMZRi7kLhzD5KlITOmjCXL2IZh7DKYjDFljzCypykhS5J1KFkrRajr90c/5+vMOdEhnXPq9Xw8rsftfK7Pua73mZvOu+uzvEWCIAggIiIiUiEayg6AiIiI6N+YoBAREZHKYYJCREREKocJChEREakcJihERESkcpigEBERkcphgkJEREQqhwkKERERqRwmKERERKRymKAQERGRylFqgrJs2TI4OztDV1cXjRs3xtGjR5UZDhEREakIpSUoW7ZsQUhICL799lucOXMGn332Gfz8/HDr1i1lhUREREQqQqSsYoHNmjWDl5cXli9fLmmrV68eevTogcjISGWERERERCpCKU9QXrx4geTkZPj6+kq1+/r64sSJE8oIiYiIiFSIUhKUBw8eoLi4GNbW1lLt1tbWyM7OVkZIREREpEK0lHlzkUgk9VoQBJk2ACgqKkJRUZFUm1gshlgs/qjxERERkXIoJUGxsLCApqamzNOSnJwcmacqABAZGYlp06ZJtYk0DKGhafxR4yQiIqKK9erFnXL1U8oQj46ODho3boz4+Hip9vj4eLRs2VKmf1hYGHJzc6UOkYZRZYVLRERElUxpQzzjx4+Hv78/mjRpghYtWmDlypW4desWRo4cKdNX3nCOvKEgIiIiqhqUlqD07dsXDx8+xA8//ICsrCy4u7tjz549cHR0VFZIREREpCKUtg/Kh9LSqansEIiIiEhBKj0HhYiIiOhtmKAQERGRymGCQkRERCqHCQoRERGpnApPUJYvX44GDRrA2NgYxsbGaNGiBfbu3Ss5LxKJ5B7z5s2r6FCIiIhITVX4Kp6dO3dCU1MTtWvXBgBERUVh3rx5OHPmDNzc3GR2j927dy8CAwNx9epV1KpVq9z34SoeIiIi9VPeVTyVsszYzMwM8+bNQ2BgoMy5Hj16ID8/HwcPHlTomkxQiIiI1E95E5SPulFbcXExtm7dioKCArRo0ULm/L1797B7925ERUV9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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(titanic.isnull(),cbar=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "66896d48",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "PassengerId    0\n",
       "Survived       0\n",
       "Pclass         0\n",
       "Name           0\n",
       "Sex            0\n",
       "Age            0\n",
       "SibSp          0\n",
       "Parch          0\n",
       "Ticket         0\n",
       "Fare           0\n",
       "Embarked       0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "8910169b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived  Pclass  \\\n",
       "0            1         0       3   \n",
       "1            2         1       1   \n",
       "\n",
       "                                                Name     Sex   Age  SibSp  \\\n",
       "0                            Braund, Mr. Owen Harris    male  22.0      1   \n",
       "1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
       "\n",
       "   Parch     Ticket     Fare Embarked  \n",
       "0      0  A/5 21171   7.2500        S  \n",
       "1      0   PC 17599  71.2833        C  "
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic.head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "ea919909",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>female</th>\n",
       "      <th>male</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   female  male\n",
       "0       0     1\n",
       "1       1     0\n",
       "2       1     0\n",
       "3       1     0\n",
       "4       0     1"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.get_dummies(titanic['Sex']).head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "ec82c593",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>male</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   male\n",
       "0     1\n",
       "1     0\n",
       "2     0"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sex=pd.get_dummies(titanic['Sex'],drop_first=True)\n",
    "sex.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "58ba9a77",
   "metadata": {},
   "outputs": [],
   "source": [
    "#we have droped the firsst coloum because onnly one coloum is sufficient to deter maine \n",
    "#the gender of the passanger "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "e84376c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "embark=pd.get_dummies(titanic['Embarked'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "e3342913",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>C</th>\n",
       "      <th>Q</th>\n",
       "      <th>S</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   C  Q  S\n",
       "0  0  0  1\n",
       "1  1  0  0\n",
       "2  0  0  1\n",
       "3  0  0  1\n",
       "4  0  0  1"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "embark.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "ceb3c8fa",
   "metadata": {},
   "outputs": [],
   "source": [
    "# C for cherbourd , q for queenstow &S for southhamptom"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "422b2662",
   "metadata": {},
   "outputs": [],
   "source": [
    "embark=pd.get_dummies(titanic['Embarked'],drop_first=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "b9104e48",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Q</th>\n",
       "      <th>S</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Q  S\n",
       "0  0  1\n",
       "1  0  0\n",
       "2  0  1"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "embark.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "a53646e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "#if both values are 0 then passanger is travling in 1 st class"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "f1e37a58",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>2</th>\n",
       "      <th>3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   2  3\n",
       "0  0  1\n",
       "1  0  0\n",
       "2  0  1"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Pcl=pd.get_dummies(titanic['Pclass'],drop_first=True)\n",
    "Pcl.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "a0ea0254",
   "metadata": {},
   "outputs": [],
   "source": [
    "#our data is now converted in to categorial data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "786fb107",
   "metadata": {},
   "outputs": [],
   "source": [
    "titanic=pd.concat([titanic,sex,embark,Pcl],axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "289cc2b3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Embarked</th>\n",
       "      <th>male</th>\n",
       "      <th>Q</th>\n",
       "      <th>S</th>\n",
       "      <th>2</th>\n",
       "      <th>3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>S</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>S</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived  Pclass  \\\n",
       "0            1         0       3   \n",
       "1            2         1       1   \n",
       "2            3         1       3   \n",
       "\n",
       "                                                Name     Sex   Age  SibSp  \\\n",
       "0                            Braund, Mr. Owen Harris    male  22.0      1   \n",
       "1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
       "2                             Heikkinen, Miss. Laina  female  26.0      0   \n",
       "\n",
       "   Parch            Ticket     Fare Embarked  male  Q  S  2  3  \n",
       "0      0         A/5 21171   7.2500        S     1  0  1  0  1  \n",
       "1      0          PC 17599  71.2833        C     0  0  0  0  0  \n",
       "2      0  STON/O2. 3101282   7.9250        S     0  0  1  0  1  "
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "2357695d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#delleting the unwanted colums "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "54d9fd71",
   "metadata": {},
   "outputs": [],
   "source": [
    "titanic.drop(['Name','PassengerId','Pclass','Ticket','Sex','Embarked'],axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "0d7cb6e0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Survived</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "      <th>male</th>\n",
       "      <th>Q</th>\n",
       "      <th>S</th>\n",
       "      <th>2</th>\n",
       "      <th>3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Survived   Age  SibSp  Parch     Fare  male  Q  S  2  3\n",
       "0         0  22.0      1      0   7.2500     1  0  1  0  1\n",
       "1         1  38.0      1      0  71.2833     0  0  0  0  0\n",
       "2         1  26.0      0      0   7.9250     0  0  1  0  1"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "bb6b207c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Train Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "03a38308",
   "metadata": {},
   "outputs": [],
   "source": [
    "X= titanic.drop('Survived',axis=1)\n",
    "y=titanic['Survived']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "25506aeb",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "90752faf",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.33,random_state=4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "8d20bea6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Logiical regressinn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "d0484272",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "lm=LogisticRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "b1ce3a72",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Acer\\anaconda3\\lib\\site-packages\\sklearn\\linear_model\\_logistic.py:458: ConvergenceWarning: lbfgs failed to converge (status=1):\n",
      "STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.\n",
      "\n",
      "Increase the number of iterations (max_iter) or scale the data as shown in:\n",
      "    https://scikit-learn.org/stable/modules/preprocessing.html\n",
      "Please also refer to the documentation for alternative solver options:\n",
      "    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression\n",
      "  n_iter_i = _check_optimize_result(\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-2 {color: black;background-color: white;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-2\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LogisticRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-2\" type=\"checkbox\" checked><label for=\"sk-estimator-id-2\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LogisticRegression</label><div class=\"sk-toggleable__content\"><pre>LogisticRegression()</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "LogisticRegression()"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lm.fit(X_train, y_train)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "99fd30f1",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_test.columns = X_test.columns.astype(str)\n",
    "prediction=lm.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "fe4068cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import confusion_matrix "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "b3c109c3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[127,  18],\n",
       "       [ 30,  60]], dtype=int64)"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "confusion_matrix(y_test,prediction)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "c3f4ad60",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import accuracy_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "c42cefcf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7957446808510639"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "accuracy_score(y_test,prediction)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "93ad5a77",
   "metadata": {},
   "outputs": [],
   "source": [
    "# we have the accuracy od 79 % which is quite good and the model can predict and data quite accuratly"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
