# Best-of-N Jailbreaking on smaller models

This is the code for the replication project described [here](https://m322.github.io/2025/01/21/bon-jailbreaking-smaller-models.html).

The prerequisites are:
* [Ollama](https://ollama.com/) installed locally and running the target models;
* an instance of [`HarmBench-Mistral-7b-val-cls`](https://huggingface.co/cais/HarmBench-Mistral-7b-val-cls) running locally via [KoboldCpp](https://github.com/LostRuins/koboldcpp) to evaluate the generations.

In addition, the following Python packages are required for the experiment and the visualizations:
* `requests`
* `pandas`
* `ollama`
* `seaborn`
