{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOsDz5+G3/LPjQvGNKObfOX",
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
        "<a href=\"https://colab.research.google.com/github/AnshuPali276/DAVIS_Claas_work/blob/main/Python_Lab/Shapes3d.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "X4zb7gaVj717"
      },
      "outputs": [],
      "source": [
        "import math\n",
        "\n",
        "# Cube\n",
        "def cube_csa(a):\n",
        "    return 4 * a * a\n",
        "\n",
        "def cube_tsa(a):\n",
        "    return 6 * a * a\n",
        "\n",
        "def cube_volume(a):\n",
        "    return a ** 3\n",
        "\n",
        "\n",
        "# Cuboid\n",
        "def cuboid_csa(l, b, h):\n",
        "    return 2 * h * (l + b)\n",
        "\n",
        "def cuboid_tsa(l, b, h):\n",
        "    return 2 * (l*b + b*h + l*h)\n",
        "\n",
        "def cuboid_volume(l, b, h):\n",
        "    return l * b * h\n",
        "\n",
        "\n",
        "# Cylinder\n",
        "def cylinder_csa(r, h):\n",
        "    return 2 * math.pi * r * h\n",
        "\n",
        "def cylinder_tsa(r, h):\n",
        "    return 2 * math.pi * r * (r + h)\n",
        "\n",
        "def cylinder_volume(r, h):\n",
        "    return math.pi * r * r * h\n",
        "\n",
        "\n",
        "# Cone\n",
        "def cone_csa(r, l):\n",
        "    return math.pi * r * l\n",
        "\n",
        "def cone_tsa(r, l):\n",
        "    return math.pi * r * (r + l)\n",
        "\n",
        "def cone_volume(r, h):\n",
        "    return (1/3) * math.pi * r * r * h\n",
        "\n",
        "\n",
        "# Sphere\n",
        "def sphere_csa(r):\n",
        "    return 4 * math.pi * r * r\n",
        "\n",
        "def sphere_tsa(r):\n",
        "    return 4 * math.pi * r * r\n",
        "\n",
        "def sphere_volume(r):\n",
        "    return (4/3) * math.pi * r ** 3\n",
        "\n",
        "\n",
        "# Hemisphere\n",
        "def hemisphere_csa(r):\n",
        "    return 2 * math.pi * r * r\n",
        "\n",
        "def hemisphere_tsa(r):\n",
        "    return 3 * math.pi * r * r\n",
        "\n",
        "def hemisphere_volume(r):\n",
        "    return (2/3) * math.pi * r ** 3"
      ]
    }
  ]
}