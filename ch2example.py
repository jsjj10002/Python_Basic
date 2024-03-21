{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1IhBYTrtEzMnATLV6t1gU5zVempA6UE2j",
      "authorship_tag": "ABX9TyO+ltOpw05hFb8hycWqSO6U"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "TPU"
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "x=100\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZhouFJD1A0zF",
        "outputId": "c9e48ce0-e881-423a-895c-9392ae020d01"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "100\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=100\n",
        "print(x)\n",
        "x=200\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QesklBISDe6g",
        "outputId": "a4478fed-94ec-4100-b9ed-6b33d44bd54b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "100\n",
            "200\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=100\n",
        "y=1200\n",
        "sum = x+y\n",
        "name = \"홍길동\"\n",
        "address = \" 서울시 종로구 1번지\"\n"
      ],
      "metadata": {
        "id": "nnDGLeyoDmCo"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(x);print(y);print(sum)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WnLr0H9VEqxg",
        "outputId": "713a8661-4f34-4657-bc30-213b3069ad7a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "100\n",
            "1200\n",
            "1300\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(name)\n",
        "print(address)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mzwvKh2dEAtu",
        "outputId": "f21f98ae-e7ae-469d-a619-e13c9f07a2ae"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "홍길동\n",
            " 서울시 종로구 1번지\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "A=17\n",
        "type(A)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "d45wiUtDFEHQ",
        "outputId": "53e6541f-2195-4acc-d29f-53776fc8b429"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'int'>\n",
            "<class 'float'>\n",
            "<class 'str'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(type(17.5))\n",
        "B='python'\n",
        "print(type(B))"
      ],
      "metadata": {
        "id": "W4jDzRZFHTdF"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "type(A)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bT7irI--EAfH",
        "outputId": "61cacac4-6eb2-472b-8517-cbdd6db2cd9c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "int"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "type(B)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xNWbZ99tG4Dv",
        "outputId": "da686a09-2cdc-4694-ea82-6fbd5f40c6e0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "str"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "type(17.5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fydR98tiG5rg",
        "outputId": "f4d0b22a-280c-4432-e3c5-7eab0f667550"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "float"
            ]
          },
          "metadata": {},
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "type([1,2,3,4])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fRUFdNsUG731",
        "outputId": "51803e43-2ac8-4ff0-f090-577a3181f1fb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "list"
            ]
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=True ;type(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2cn-0XwPG-3W",
        "outputId": "bd8cd9dc-8355-431f-bb3d-241939ed1a9e"
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
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=bool(1);type(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "27oF_FWLHqIG",
        "outputId": "a36ad24b-1e48-41a0-8486-b1a8c0700246"
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
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "type(int(a))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2_fb6T5aHuZ-",
        "outputId": "5f2d52d8-5dd1-43c8-f5a9-f3ae8e316ca7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "int"
            ]
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x= int(input(\"input first real number\"))\n",
        "y= int(input(\"input second real number\"))\n",
        "sum=x+y;print(\"x+y=\",sum)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KU6Dm_B2HzV2",
        "outputId": "1bb69ccf-e5fe-44b3-f010-4a96045f1ca1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "input first real number100\n",
            "input second real number200\n",
            "x+y= 300\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "name=str(input('input your name: '))\n",
        "print(name,', hello')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zdXhI4QVH3vW",
        "outputId": "56158126-f4e2-43bf-bb02-c0725eb865ff"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "input your name: a\n",
            "a , hello\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "name=input(\"input your name:\")\n",
        "\n",
        "height=int(input(\"inout yuor height:\"))\n",
        "weight=int(input(\"input yuor weight:\"))\n",
        "bmi=weight/(height**2)\n",
        "print(\"%s's bmi is %02f\"%(name, bmi))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jF3Elz31Jyr0",
        "outputId": "450850af-9c2a-408e-edd5-13253e50978c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "input your name:js\n",
            "inout yuor height:177\n",
            "input yuor weight:95\n",
            "js's bmi is 0.003032\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "GQ4xifjRMqJq"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}