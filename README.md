# execution-scenarios
The code collected in this repository started as a set of local experiments while testing various transaction flows and execution scenarios. Over time, some of these utilities became useful enough to keep together in a single workspace.

Several examples investigate how an aggregator can combine information coming from different sources before a transaction is prepared. The purpose is not to simulate real markets, but to demonstrate how multiple inputs may influence execution decisions.

Some test cases focus on selecting optimal prices under changing conditions. These experiments help evaluate how applications react to delays, changing parameters, and external data sources.

Another recurring topic is slippage. Small differences between expected and actual execution values can significantly affect transaction behavior, so several utilities include simple monitoring and reporting mechanisms.

Most scripts inside this repository are intentionally small and somewhat independent from each other. They were written to test ideas, compare different approaches, and provide practical examples that can be modified without understanding an entire framework.
