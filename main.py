{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNIe1+gkn02SwHBCib/uIw+",
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
        "<a href=\"https://colab.research.google.com/github/BooTheGh0st/Lab11FileOutput/blob/main/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from functools import partial\n",
        "from random import sample, randint, shuffle, choices\n",
        "from util import cost, best_path, valid_path\n",
        "\n",
        "# Safe cost function to handle None values in cost results\n",
        "def safe_cost(path, distances):\n",
        "    result = cost(path, distances)\n",
        "    return float('inf') if result is None else result\n",
        "\n",
        "def ga_tsp(initial_population, distances, generations):\n",
        "    # Check for None or invalid arguments\n",
        "    if initial_population is None or distances is None or generations is None or generations <= 0:\n",
        "        return None\n",
        "\n",
        "    # Filter valid paths in the initial population\n",
        "    population = [path for path in initial_population if valid_path(path) and cost(path, distances) is not None]\n",
        "\n",
        "    # Ensure there is a valid population to work with\n",
        "    if not population:\n",
        "        raise ValueError(\"No valid initial population paths found\")\n",
        "\n",
        "    for generation in range(generations):\n",
        "        # Step 1: Calculate fitness and select parents based on safe cost function\n",
        "        fitness_population = sorted(population, key=partial(safe_cost, distances))\n",
        "\n",
        "        # Step 2: Crossover - create new paths from pairs of selected parents\n",
        "        children = []\n",
        "        while len(children) < len(population):  # Maintain steady population size\n",
        "            parent1, parent2 = select_parents(fitness_population, distances)\n",
        "            child1, child2 = crossover(parent1, parent2)\n",
        "            children.append(child1)\n",
        "            if len(children) < len(population):\n",
        "                children.append(child2)\n",
        "\n",
        "        # Step 3: Mutation - randomly mutate children\n",
        "        children = [mutate(child) for child in children]\n",
        "\n",
        "        # Step 4: Create the new generation by selecting the best paths\n",
        "        population = sorted(population + children, key=partial(safe_cost, distances))[:len(population)]\n",
        "\n",
        "    # Return the best path from the final generation\n",
        "    return best_path(population, distances)\n",
        "\n",
        "# Updated select_parents function with safe cost\n",
        "def select_parents(population, distances):\n",
        "    parent1 = min(choices(population, k=5), key=partial(safe_cost, distances))\n",
        "    parent2 = min(choices(population, k=5), key=partial(safe_cost, distances))\n",
        "    return parent1, parent2\n",
        "\n",
        "def crossover(parent1, parent2):\n",
        "    size = len(parent1)\n",
        "    start, end = sorted(sample(range(size), 2))  # Random crossover points\n",
        "\n",
        "    child1 = [None] * size\n",
        "    child2 = [None] * size\n",
        "\n",
        "    # Copy a slice from each parent to the child\n",
        "    child1[start:end] = parent1[start:end]\n",
        "    child2[start:end] = parent2[start:end]\n",
        "\n",
        "    # Fill remaining cities from the other parent\n",
        "    fill_child(child1, parent2, start, end)\n",
        "    fill_child(child2, parent1, start, end)\n",
        "\n",
        "    return tuple(child1), tuple(child2)\n",
        "\n",
        "def fill_child(child, parent, start, end):\n",
        "    size = len(child)\n",
        "    i, j = end, end\n",
        "    while None in child:\n",
        "        if parent[j % size] not in child:\n",
        "            child[i % size] = parent[j % size]\n",
        "            i += 1\n",
        "        j += 1\n",
        "\n",
        "def mutate(path, mutation_rate=0.1):\n",
        "    path = list(path)\n",
        "    # Only mutate based on the mutation rate\n",
        "    if randint(1, 100) <= mutation_rate * 100:\n",
        "        # Choose two random indices to swap\n",
        "        idx1, idx2 = sample(range(len(path)), 2)\n",
        "        # Perform the swap mutation\n",
        "        path[idx1], path[idx2] = path[idx2], path[idx1]\n",
        "\n",
        "    return tuple(path)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 384
        },
        "id": "g0yZ0cWnpJ1R",
        "outputId": "4b0db6af-07c9-4a8f-e7bc-0d7d301f998d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "No module named 'util'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-3-f4d5bd6abb2c>\u001b[0m in \u001b[0;36m<cell line: 3>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mfunctools\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpartial\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mrandom\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0msample\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mrandint\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mshuffle\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mchoices\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mutil\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mcost\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbest_path\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mvalid_path\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;31m# Safe cost function to handle None values in cost results\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'util'",
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
      ]
    }
  ]
}