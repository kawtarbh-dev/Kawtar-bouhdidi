{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM2uDTeg2irmKAiOKHHDL8P",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/kawtarbh-dev/Kawtar-bouhdidi/blob/main/Personal_expense_tracker.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Hello World"
      ],
      "metadata": {
        "id": "0ECzBOF9IqJv"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LECu2aNHEgsO",
        "outputId": "3891a8f4-ef8c-4c80-cdab-3c427471fd9a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hello, world!\n"
          ]
        }
      ],
      "source": [
        "print('hello, world!')"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Variables"
      ],
      "metadata": {
        "id": "aLgmP14mI6S9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"there once was a man named Ali\")\n",
        "print(\"he was 50 years old\")\n",
        "print(\"he really liked the name Ali\")\n",
        "print(\"but didn't like being 50\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tQzSslJQEjq8",
        "outputId": "b64ba8fe-1035-4261-d605-a31ff59f1059"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "there once was a man named Ali\n",
            "he was 50 years old\n",
            "he really liked the name Ali\n",
            "but didn't like being 50\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "name=\"10\"\n",
        "age= 10\n",
        "print(\"there once was a man named \" + name)\n",
        "print(\"he was \" + str(age) + \" years old\")\n",
        "print(\"he really liked the name \" + name)\n",
        "print(\"but didn't like being \" + str(age))\n",
        "print(f\"{name} is {age} years old\")\n",
        "print(\"{} is {} years old\".format(name,age))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jQquY0jWEjtT",
        "outputId": "37e25363-ca10-43ed-ab94-4c12dfbbf03d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "there once was a man named 10\n",
            "he was 10 years old\n",
            "he really liked the name 10\n",
            "but didn't like being 10\n",
            "10 is 10 years old\n",
            "10 is 10 years old\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "name=True\n",
        "type(name)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DenXrAMYLo8O",
        "outputId": "6842446e-0101-46ae-b408-e5aa1b03bb78"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "bool"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "String"
      ],
      "metadata": {
        "id": "OZT2t6FGM3gW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "phrase = \"Ali is 20 years old\""
      ],
      "metadata": {
        "id": "7E8P_vTTLo-y"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(phrase.upper())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hMYzwPyxLpBk",
        "outputId": "5e8cab84-db88-4023-a91d-89bf14b578b6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ALI IS 20 YEARS OLD\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(phrase.lower())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pen3Bs1NLpEI",
        "outputId": "537cc5b9-f6c5-4bec-b9a7-54b5748e9f8e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ali is 20 years old\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "len(phrase)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YboDoOHGLpGf",
        "outputId": "6ea1c489-6906-49d9-fa30-dd3637df4b5f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "19"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(phrase.replace(\"Ali\",\"mohamed\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0CvnJi-LEjvi",
        "outputId": "368f9d67-6696-40b4-869c-cce4eceac209"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "mohamed is 20 years old\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "phrase[0]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "qttJEENEEjx5",
        "outputId": "349f62e9-a565-4fa1-ba37-fe24336b5815"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'A'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "phrase[-1]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "NLXexbbjNy55",
        "outputId": "921b0f4e-006c-4c07-c6b6-cb5e657e5ef9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'d'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "phrase[0:3]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "X3dBbs7fNy8X",
        "outputId": "fbc79386-16c1-4325-e36b-7b17d306271c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Ali'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "phrase.index('A')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5HXuBnLGNzAp",
        "outputId": "79cb0b0a-3268-42e5-f385-2507ae7ba39d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Operators"
      ],
      "metadata": {
        "id": "Wy6hxIouOHPB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(2 * 3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3kGByCBBNzC3",
        "outputId": "3f524697-903e-4aa5-e118-0b0830f49a91"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "6\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(25 / 5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Np5_P8I_NzFU",
        "outputId": "11585e82-e71c-4acd-84cb-b02b824a8c6b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(10 % 3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LMUmXwhRNzHr",
        "outputId": "0858943a-8091-4b3c-b81f-b90f42cf5c09"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(2 ** 2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mGffzQwNNzKB",
        "outputId": "9ef1b36b-53a3-478c-946f-aa8f77dfb4c9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from math import sqrt\n",
        "sqrt(16)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JeBnXfPGNzMU",
        "outputId": "060af97c-fa85-4f1d-d051-c57b921478a1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "4.0"
            ]
          },
          "metadata": {},
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "try:\n",
        "  a = float(input('Enter a numerical value: '))\n",
        "  b = float(input('Enter a numerical value: '))\n",
        "  print(a + b)\n",
        "except ValueError:\n",
        "  print(\"Invalid input. Please enter numerical values.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OAZKhZdlNzOz",
        "outputId": "ade87a05-2ec3-4ea6-bf79-a298fa632479"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a numerical value: 20\n",
            "Enter a numerical value: 10\n",
            "30.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Numbers"
      ],
      "metadata": {
        "id": "3-z16KbDPs0D"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "x = -2\n",
        "abs(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MfrmIDLSPobI",
        "outputId": "931d7cc9-00d0-42f9-c3e1-1c5d0fbb5f00"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2"
            ]
          },
          "metadata": {},
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x ** 3"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oXUp4eTUPod3",
        "outputId": "e4811130-f410-4484-b886-ec4e11c659b7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "-8"
            ]
          },
          "metadata": {},
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pow(x, 3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9U_WpX9IQNw6",
        "outputId": "23042819-cdb7-41e4-fc14-10fd175445f7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "-8"
            ]
          },
          "metadata": {},
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from math import sqrt\n",
        "sqrt(abs(x))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oGQG-kinPogm",
        "outputId": "5fd300ae-eb76-4bb4-df84-46b71311cf1c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1.4142135623730951"
            ]
          },
          "metadata": {},
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "round(3.2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cgaZXwTuPoke",
        "outputId": "32537963-b1f1-45b0-e8dc-6fa919c4a0af"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3"
            ]
          },
          "metadata": {},
          "execution_count": 34
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from math import *"
      ],
      "metadata": {
        "id": "O5dOS99JPoo9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "floor(3.6)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "K08mBAX9Porg",
        "outputId": "671a1edb-b9c0-4b7d-ea82-1305f71d2a33"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3"
            ]
          },
          "metadata": {},
          "execution_count": 36
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "ceil(3.2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6WEt7iwSPpa6",
        "outputId": "90d01cb2-ad48-4dd3-ef04-bf5435229926"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "4"
            ]
          },
          "metadata": {},
          "execution_count": 37
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"20\"+\"30\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0aAzDw_mPpdl",
        "outputId": "9fcd8966-f2e8-4322-efba-e2719b554c61"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2030\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "List"
      ],
      "metadata": {
        "id": "gyJgWyM4Q2mA"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "students = ['ali','mohamed','ahmed']"
      ],
      "metadata": {
        "id": "IwYx5Q9iPpga"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "students[1:3]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iicc6DONPpjT",
        "outputId": "4cf73c22-49d6-467c-d483-136f14119e55"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['mohamed', 'ahmed']"
            ]
          },
          "metadata": {},
          "execution_count": 40
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "students"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zfr9z_KdPpmG",
        "outputId": "88fe9707-0196-4960-8846-53958ece75f7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['ali', 'mohamed', 'ahmed']"
            ]
          },
          "metadata": {},
          "execution_count": 41
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "etu = [\"mark\", \"omar\"]"
      ],
      "metadata": {
        "id": "gYMB_s9qRORN"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "students.extend(etu)"
      ],
      "metadata": {
        "id": "rmnnAhqnROUX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "students"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5joz6h_-ROXi",
        "outputId": "be4205bc-df58-4ffb-e37d-192dd00fe724"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['ali', 'mohamed', 'ahmed', 'mark', 'omar']"
            ]
          },
          "metadata": {},
          "execution_count": 44
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "students.append(\"ahmed\")"
      ],
      "metadata": {
        "id": "38TxogyeRv5i"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "students.insert(1, \"ilyas\")"
      ],
      "metadata": {
        "id": "tGM26sc_RvwT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "students"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iyt9QIT2ROam",
        "outputId": "dad52935-e8af-4bd8-f95f-15bb54ec5e1f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['ali', 'mohamed', 'ahmed', 'mark', 'omar']"
            ]
          },
          "metadata": {},
          "execution_count": 45
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "students[0:2]='ahmed'"
      ],
      "metadata": {
        "id": "HewLqpaVROd3"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "students[2]='omar'"
      ],
      "metadata": {
        "id": "qdb6BeA0ROgz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "students.count('ali')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CCx78RdhROko",
        "outputId": "0e04d52b-b95a-4ed6-b434-298a09fbba2b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0"
            ]
          },
          "metadata": {},
          "execution_count": 51
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "students.pop()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "VQOYQ0_yROoc",
        "outputId": "1bbf3b06-488b-4ef3-c4ab-85749eff62b5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'ahmed'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 52
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "students.remove('ahmed')"
      ],
      "metadata": {
        "id": "63ZCOj0LSqs5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "students.append('ahmed') # Add 'ahmed' back to the list\n",
        "students.index('ahmed')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KltJBvPISqwY",
        "outputId": "f6a74986-3bc9-40ad-c2c0-2f1ce11a03a7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "8"
            ]
          },
          "metadata": {},
          "execution_count": 55
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "students.sort()"
      ],
      "metadata": {
        "id": "5JEcdfZ_Sqz6"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "numbers = [-10, 20, 0, 100]"
      ],
      "metadata": {
        "id": "wx-40q93Sq3R"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "numbers.sort()"
      ],
      "metadata": {
        "id": "450tir0TSq6t"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "numbers"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "z0CZEnnBSq9p",
        "outputId": "876e3bd7-3a43-4679-afb2-0566eb1a4c68"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[-10, 0, 20, 100]"
            ]
          },
          "metadata": {},
          "execution_count": 59
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "numbers.reverse()"
      ],
      "metadata": {
        "id": "hh_JXD4FSrA8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "num = numbers.copy()"
      ],
      "metadata": {
        "id": "DQDJUzn8SrEH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "num"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NFK05TElSrHh",
        "outputId": "c72d6cc6-3532-4f8b-8414-121eed362141"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[100, 20, 0, -10]"
            ]
          },
          "metadata": {},
          "execution_count": 62
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "numbers"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WkX5r-gCSrKl",
        "outputId": "ed47f77a-19ae-426a-cd66-edb28953e82f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[100, 20, 0, -10]"
            ]
          },
          "metadata": {},
          "execution_count": 63
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "numbers.append(20)"
      ],
      "metadata": {
        "id": "Xe6geaV6SrOR"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "numbers.count(0)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LhChi724SrRg",
        "outputId": "20ae50d1-eeb2-4f20-e73f-d987b4fb0a18"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1"
            ]
          },
          "metadata": {},
          "execution_count": 65
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "L = [\"ali\", 20, 10.5, True]"
      ],
      "metadata": {
        "id": "FpDTtqG3SrUr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "L[0]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "ZYUBHSYrSrYC",
        "outputId": "2e330a81-9895-4554-ff2f-b1629ee01862"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'ali'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 67
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Tuple"
      ],
      "metadata": {
        "id": "CPeEtBeEUi2b"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "coordinates = (4, 5)"
      ],
      "metadata": {
        "id": "P6EZ8euOSrbO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "coordinates=(2, 3, 6)"
      ],
      "metadata": {
        "id": "du18RnPGSren"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "coordinates"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "z3wMwoAKROrl",
        "outputId": "28d2860a-9c15-43cc-a91f-92ca27fbf6e4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(2, 3, 6)"
            ]
          },
          "metadata": {},
          "execution_count": 70
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "coordinates.index(2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kMm6-0BlROul",
        "outputId": "fa326f6b-bce0-498f-82b0-002b37905246"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0"
            ]
          },
          "metadata": {},
          "execution_count": 71
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "len(coordinates)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jiMYKz-jU8eJ",
        "outputId": "f0c42291-499b-4e74-ac32-ace2af5bee79"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3"
            ]
          },
          "metadata": {},
          "execution_count": 72
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "type(coordinates)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "u10WyOsAU8iP",
        "outputId": "8ece15d3-a6b2-4d0a-9cd1-7c02269295a4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tuple"
            ]
          },
          "metadata": {},
          "execution_count": 74
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "tuples_list = [(2, 5), ('ahmeed',20), ('Ali', True)]"
      ],
      "metadata": {
        "id": "QWFZeKCKU8ne"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "tuples_list[0]= 'Ahmed'"
      ],
      "metadata": {
        "id": "YFDKxU5vU8ro"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "tuples_list"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PxyLf_P5U8vg",
        "outputId": "f1bb964a-0694-46c5-8de6-0ab51d128ef4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Ahmed', ('ahmeed', 20), ('Ali', True)]"
            ]
          },
          "metadata": {},
          "execution_count": 77
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "numbers = [10, 5, 2]"
      ],
      "metadata": {
        "id": "LfULcnudU8zP"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "num = tuple(numbers)"
      ],
      "metadata": {
        "id": "C097G2ATU82i"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "num"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hy-qUkqAWBe7",
        "outputId": "5cf13751-b332-4869-f23f-652be84c55d1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(10, 5, 2)"
            ]
          },
          "metadata": {},
          "execution_count": 81
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Functions"
      ],
      "metadata": {
        "id": "-4p4Sq7RWF3O"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "nom = 'ahmed'\n",
        "print(\"hello\", nom)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DLFl0UPyWBjR",
        "outputId": "145eecef-a9d7-49ca-cbfa-762529a750fe"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hello ahmed\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def say_hello(a, b, op):\n",
        "  print(\"hello\", a, \"you are \", b, \"years old\")\n",
        "  print(\"goodbye\", a)"
      ],
      "metadata": {
        "id": "I84S-ifxWBnW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "name= input(\"enter your name:\")\n",
        "age= input(\"enter your age: \")\n",
        "say_hello(name, age, None)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZWTV-43JWBuI",
        "outputId": "32c4a585-c77d-49eb-f78f-cedfd77a27eb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter your name:ahmed\n",
            "enter your age: 21\n",
            "hello ahmed you are  21 years old\n",
            "goodbye ahmed\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('before')\n",
        "def square(a):\n",
        "  print('after')\n",
        "  return a*a"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ESGHZWZiXbJX",
        "outputId": "a613bc03-9e01-416e-9e27-15b5ce552aad"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "before\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "calc = 10+square(2)\n",
        "calc"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HaLH4NNdPpoz",
        "outputId": "4775b31c-a277-4586-8f59-17b5530cd970"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "after\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "14"
            ]
          },
          "metadata": {},
          "execution_count": 87
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def aged(a):\n",
        "  print(\"Your age after 10 years\")"
      ],
      "metadata": {
        "id": "8NUIUAD2YjkV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "age = int(input(\"Enter your age:\"))\n",
        "aged(age)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cd3-MR6wYjoz",
        "outputId": "ce52f4d2-9cac-4873-afd3-62d418793f56"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your age:20\n",
            "Your age after 10 years\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "iF Statements"
      ],
      "metadata": {
        "id": "3_yWKdRjY__r"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a=10\n",
        "b=2\n",
        "\n",
        "if b!=0:\n",
        "  if a%b==0:\n",
        "    print(f\"{a} is divisible by {b}\")\n",
        "  else:\n",
        "    print(f\"{a} is not divisible by {b}\")\n",
        "else:\n",
        "    print(\"error\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5D0Mly48Yjtc",
        "outputId": "2f5ef6e6-7c3c-470b-8e80-6c15a288c22e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10 is divisible by 2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def calc(a, b, op):\n",
        "  if op == '+':\n",
        "    print(a+b)\n",
        "  elif op == '-':\n",
        "    print(a-b)\n",
        "  elif op == '*':\n",
        "    print(a*b)\n",
        "  elif op == '/':\n",
        "    if b!=0:\n",
        "      print(a/b)\n",
        "    else:\n",
        "      print('division by zero')\n",
        "  else:\n",
        "    print(\"Invalid operator\")"
      ],
      "metadata": {
        "id": "Z_p6nFM7Yjxy"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "num1 = float(input(\"Enter first number: \"))\n",
        "operator  = input(\"Enter operator:\")\n",
        "num2 = float(input(\"Enter second number: \"))\n",
        "calc(num1, num2, operator)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f9qjSYpOYj4G",
        "outputId": "fa8047da-7480-41b2-fbc5-ff2b31c4d9bc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter first number: 21\n",
            "Enter operator:/\n",
            "Enter second number: 2\n",
            "10.5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "is_adult = False\n",
        "if False:\n",
        "  print(\"You are an adult\")"
      ],
      "metadata": {
        "id": "z_57Ng_NcGjk"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "While Loop"
      ],
      "metadata": {
        "id": "T7XDaFUQcYZJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "x=0\n",
        "while x<10 and x!=0:\n",
        "  print(x)\n",
        "  x=x+1"
      ],
      "metadata": {
        "id": "rpAeqgUpcWXy"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Guessing Game"
      ],
      "metadata": {
        "id": "nv-jHxt4agWh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "secret = 'cat'\n",
        "guess = ''\n",
        "limit = 3\n",
        "count = 0\n",
        "out_of_guesses = False\n",
        "\n",
        "while guess != secret and out_of_guesses:\n",
        "  if count < limit:\n",
        "    guess = input('Enter guess: ')\n",
        "    count += 1\n",
        "  else:\n",
        "    out_of_guesses = True\n",
        "\n",
        "if out_of_guesses:\n",
        "  print('You Lost')\n",
        "else:\n",
        "  print('You Won!')\n"
      ],
      "metadata": {
        "id": "_D-mQU0DcWdK",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "dfbe8ba6-df6b-4175-b82a-2d34da4be5cb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "You Won!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "For Loop"
      ],
      "metadata": {
        "id": "ppLzLIFWbWt2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1,10,2):\n",
        "  print(i)"
      ],
      "metadata": {
        "id": "LAO-kdWsMOES",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "22ffc887-6ce2-49b9-9e63-b57c5b519966"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "3\n",
            "5\n",
            "7\n",
            "9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for char in 'Ali is 20':\n",
        "  print(char)"
      ],
      "metadata": {
        "id": "m_qtDOhiMOIc",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c184bc5b-e6e2-4e48-adef-4721433a4513"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "A\n",
            "l\n",
            "i\n",
            " \n",
            "i\n",
            "s\n",
            " \n",
            "2\n",
            "0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "students = ['ali', 'mohammed', 'ahmed']\n",
        "students.sort()\n",
        "for item in students:\n",
        "  print(item)"
      ],
      "metadata": {
        "id": "-nXekCHGMOMZ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5151e50e-7273-4ea4-fb0b-ab58ff1ab3ac"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ahmed\n",
            "ali\n",
            "mohammed\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Nested List"
      ],
      "metadata": {
        "id": "lTO8hIxTcQ_1"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "Nested_list = [['Ali', 20], ['mohammed', 21], ['ahmed', 22]]"
      ],
      "metadata": {
        "id": "bGHUWFRXMOQV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "Nested_list[1][1]"
      ],
      "metadata": {
        "id": "heNxGeV5MOU5",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "11ecbe88-b50d-497f-e357-bad6496aa854"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "21"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Dictionaries"
      ],
      "metadata": {
        "id": "z1BZyMdFcrQU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "months = {'Jan': 'January', 'Feb': 'February', 'Mar': 'March'}"
      ],
      "metadata": {
        "id": "QdAbjRPiMOZZ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "months['Mar']"
      ],
      "metadata": {
        "id": "oXdTY2q8MOdZ",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "e897f435-c8de-4ac8-e06c-728ddf74d246"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'March'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Simple Translator"
      ],
      "metadata": {
        "id": "ijMkCkXLdF0Z"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "word=\"dog\"\n",
        "translation = \"\"\n",
        "\n",
        "for char in word:\n",
        "  if char in \"aeiou\":\n",
        "    translation = translation + \"g\"\n",
        "  else:\n",
        "    translation = translation + char\n",
        "\n",
        "print(translation)"
      ],
      "metadata": {
        "id": "bIFw-5xAMOgx",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0872d0e4-108a-4ce9-e010-7e850a24a07e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "dgg\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Error Handling Try Except"
      ],
      "metadata": {
        "id": "need4Sdmdacm"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "try:\n",
        "  a = int(input(\"Enter 1st number: \"))\n",
        "  b = input(\"Enter 2nd number: \")\n",
        "  print(a/b)\n",
        "except Exception as e:\n",
        "  print(\"Program continues\")\n",
        "  a=10+2\n",
        "  print(a)\n"
      ],
      "metadata": {
        "id": "iIqBQwFGMOkT",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0ba619ea-1c4d-4b72-a2aa-2226af0e831e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter 1st number: 10\n",
            "Enter 2nd number: 2\n",
            "Program continues\n",
            "12\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "try:\n",
        "  a = int(input(\"Enter 1st number: \"))\n",
        "  b = int(input(\"Enter 2nd number: \"))\n",
        "  print(a/b)\n",
        "except ZeroDivisionError:\n",
        "  print(\"Error: Cannot divide by zero.\")\n",
        "except ValueError:\n",
        "  print(\"Invalid input. Please enter integers.\")"
      ],
      "metadata": {
        "id": "6scCROLeMOoX",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "946d9d24-0e88-42f8-feee-87dd9e2d741c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter 1st number: 10\n",
            "Enter 2nd number: 0\n",
            "Error: Cannot divide by zero.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "The personal expense tracker"
      ],
      "metadata": {
        "id": "QfryfdSHty2K"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "expenses = []\n",
        "def add_expense():\n",
        "  print(\"\\n--- Add a New Expense --- \")\n",
        "  while True: # Added colon here\n",
        "    try:\n",
        "      amount = float(input(\"Enter expense amount:\"))\n",
        "      break\n",
        "    except ValueError:\n",
        "      print(\"Invalid input. Please enter a number.\")\n",
        "  category = input(\"Enter expense category:\")\n",
        "  expense = {\"Amount\":amount, \"Category\":category} # Changed '=' to ':'\n",
        "  expenses.append(expense)\n",
        "  print(\"Expense added successfully!\\n\")\n",
        "\n",
        "def view_expenses():\n",
        "        print(\"\\n--- Expenses ---\") # Changed /n to \\n\n",
        "        if not expenses:\n",
        "          print(\"No expenses recorded yet.\\n\") # Changed /n to \\n\n",
        "        else:\n",
        "            for i, expense in enumerate(expenses, start=1):\n",
        "              print(f\"{i}. {expense['Category']}: {expense['Amount']:.2f}\")\n",
        "        print() # Added print() outside the loop\n",
        "\n",
        "def calculate_total():\n",
        "  print(\"\\n--- Total Expense ---\") # Changed /n to \\n\n",
        "  if not expenses:\n",
        "    print(\"No expenses recorded yet.\\n\") # Changed /n to \\n\n",
        "  else:\n",
        "      total = sum(expense[\"Amount\"] for expense in expenses)\n",
        "      print(f\"Total expenses: {total:.2f}\")\n",
        "\n",
        "def main():\n",
        "  print(\"Welcome to the personal Expense Tracker!\") # Corrected spelling\n",
        "  while True:\n",
        "    print(\"\\n1. Add Expense\")\n",
        "    print(\"2. View Expenses\")\n",
        "    print(\"3. Calculate Total\")\n",
        "    print(\"4. Quit\")\n",
        "    choice = input(\"Enter your choice (1/2/3/4):\")\n",
        "\n",
        "    if choice == \"1\":\n",
        "        add_expense() # Corrected indentation\n",
        "    elif choice == \"2\":\n",
        "        view_expenses() # Corrected indentation\n",
        "    elif choice == \"3\":\n",
        "        calculate_total() # Corrected indentation\n",
        "    elif choice == \"4\":\n",
        "        print(\"Goodbye!\")\n",
        "        break # Corrected indentation\n",
        "    else:\n",
        "        print(\"Invalid choice. Please select a valid option (1/2/3/4).\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main() # Corrected indentation"
      ],
      "metadata": {
        "id": "m9s1KD7JeafX",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b9b866a0-3426-41a1-a3d2-05ff93768697"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Welcome to the personal Expense Tracker!\n",
            "\n",
            "1. Add Expense\n",
            "2. View Expenses\n",
            "3. Calculate Total\n",
            "4. Quit\n",
            "Enter your choice (1/2/3/4):4\n",
            "Goodbye!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "UREDK_NaeajT"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}