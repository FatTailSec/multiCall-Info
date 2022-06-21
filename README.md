# multiCall-Info
Two scripts which will batch txns to a multicall contract to query on chain data


How to use:

1) Install dependencies 
```
pip install -r requirements.txt || pip3 install -r requirements.txt
```

2) Instantiate the Infura provider 
```
export WEB3_INFURA_PROJECT_ID=4d1481d1a4c04cb4a9646260001f072f
```

3) To run the multicall script on the eth network 
```
brownie run scripts/multiCall-eth.py --network mainnet
```

4) To run the multicall script on the ftm network 
```
brownie run scripts/multiCall-ftm.py --network ftm-main
```

The CSV files will be created in the directory accordingly
