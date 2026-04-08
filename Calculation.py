{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMWyjZNX0d+k1QXjNrrUKXT",
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
        "<a href=\"https://colab.research.google.com/github/AnshuPali276/DAVIS_Claas_work/blob/main/Calculation.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "   To import entire Module\n",
        "Syntax: import modulename\n",
        "\n",
        "  to call the fuction\n",
        "Syntax: modulename.function_name(parameter)"
      ],
      "metadata": {
        "id": "kA-NQIiKSEFS"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 383
        },
        "id": "lumgkxH8SBQE",
        "outputId": "47fd423e-5931-46e1-c974-2dae998e7401"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "No module named 'NumericCalculate'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipykernel_2403/4242394704.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m#To import entire function\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mNumericCalculate\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m \u001b[0mm\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m10\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mn\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m20\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"sum of\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mm\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\"and\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mn\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\"is:\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mNumericCalculate\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0maddNumbers\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mm\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mn\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'NumericCalculate'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ],
      "source": [
        "#To import entire function\n",
        "import NumericCalculate\n",
        "m=10\n",
        "n=20\n",
        "print(\"sum of\",m,\"and\",n,\"is:\",NumericCalculate.addNumbers(m,n))\n",
        "print(\"Product of\",m,\"and\",n,\"is:\",NumericCalculate.claculateproduct(m,n))\n",
        "\n"
      ]
    }
  ]
}