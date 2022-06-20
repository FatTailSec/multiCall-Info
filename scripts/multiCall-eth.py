from brownie import Contract, interface, multicall, web3
import csv
import os
from dotenv import load_dotenv 

load_dotenv()

def main():
    yearnVaultList = [
        "0xa354F35829Ae975e850e23e9615b11Da1B3dC4DE", #USDC Vault
        "0xdA816459F1AB5631232FE5e97a05BBBb94970c95", #DAI Vault
        "0xa258C4606Ca8206D8aA700cE2143D7db854D168c", #ETH Vault
        "0xdCD90C7f6324cfa40d7169ef80b12031770B4325", #Curve stETH Pool yVault
        "0x27b7b1ad7288079A66d12350c828D3C00A6F07d7", #Curve Iron Bank Pool
        "0xd88dBBA3f9c4391Ee46f5FF548f289054db6E51C", #Curve DOLA Pool
        "0x3B96d491f067912D18563d56858Ba7d6EC67a6fa", #Curve USDN Pool
        "0xA696a63cc78DfFa1a63E9E50587C197387FF6C7E", #WBTC yVault 
        "0x5faF6a2D186448Dfa667c51CB3D695c7A6E52d8E", #Curve stETH-WETH Pool
        "0x5fA5B62c8AF877CB37031e0a3B2f34A78e3C56A6", #Curve LUSD Pool 
        "0xdb25cA703181E7484a155DD612b06f57E12Be5F0", #YFI yVault
        "0xE537B5cc158EB71037D4125BDD7538421981E6AA", #Curve 3Crypto Pool 
        "0xC4dAf3b5e2A9e93861c3FBDd25f1e943B8D87417", #Curve USDP Pool
        "0xB4AdA607B9d6b2c9Ee07A275e9616B84AC560139", #Curve FRAX Pool 
        "0xA74d4B67b3368E83797a35382AFB776bAAE4F5C8", #Curve alUSD Pool 
        "0x378cb52b00F9D0921cb46dFc099CFf73b42419dC", #LUSD yVault (LUSD)
        "0xF29AE508698bDeF169B89834F76704C3B205aedf", #SNX yVault (SNX)
        "0x625b7DF2fa8aBe21B0A976736CDa4775523aeD1E", #Curve HBTC Pool yVault (Curve HBTC)
        "0xd9788f3931Ede4D5018184E198699dC6d66C1915", #AAVE yVault (AAVE)
        "0x2DfB14E32e2F8156ec15a2c21c3A6c053af52Be8", #Curve MIM Pool yVault (Curve MIM)
        "0x6Ede7F19df5df6EF23bD5B9CeDb651580Bdf56Ca", #Curve BUSD Pool yVault (Curve BUSD)
        "0x986b4AFF588a109c09B50A03f42E4110E29D353F", #Curve sETH Pool yVault (Curve sETH)
        "0x8414Db07a7F743dEbaFb402070AB01a4E0d2E45e", #Curve sBTC Pool yVault (Curve sBTC)
        "0x2D5D4869381C4Fce34789BC1D38aCCe747E295AE", #Curve RAI Pool yVault (Curve RAI)
        "0x5a770DbD3Ee6bAF2802D29a901Ef11501C44797A", #Curve sUSD Pool yVault (Curve sUSD)
        "0xBfedbcbe27171C418CDabC2477042554b1904857", #Curve rETH Pool yVault (Curve rETH)
        "0x5AB64C599FcC59f0f2726A300b03166A395578Da", #Curve 3EUR Pool yVault (Curve 3EUR)
        "0x8cc94ccd0f3841a468184aCA3Cc478D2148E1757", #Curve mUSD Pool yVault (Curve mUSD)
        "0x2a38B9B0201Ca39B17B460eD2f11e4929559071E", #Curve GUSD Pool yVault (Curve GUSD)
        "0x6A5468752f8DB94134B6508dAbAC54D3b45efCE6", #Curve CRV-ETH Pool yVault (Curve CRV-ETH)
        "0xb4D1Be44BfF40ad6e506edf43156577a3f8672eC", #Curve sAave Pool yVault (Curve sAave)
        "0xFBEB78a723b8087fD2ea7Ef1afEc93d35E8Bed42", #UNI yVault (UNI)
        "0x6d765CbE5bC922694afE112C140b8878b9FB0390", #SUSHI yVault (SUSHI)
        "0x1635b506a88fBF428465Ad65d00e8d6B6E5846C3", #Curve CVX-ETH Pool yVault (Curve CVX-ETH)
        "0x790a60024bC3aea28385b60480f15a0771f26D09", #Curve YFI-ETH Pool yVault (Curve YFI-ETH)
        "0xBCBB5b54Fa51e7b7Dc920340043B203447842A6b", #Curve EURT-USD Pool yVault (Curve EURT-USD)
        "0x132d8D2C76Db3812403431fAcB00F3453Fc42125", #Curve ankrETH Pool yVault (Curve aETHc)
        "0x4560b99C904aAD03027B5178CCa81584744AC01f", #Curve cvxCRV Pool yVault (Curve cvxCRV)
        # All other yearn vaults were less than 100k TVL
        "0x16825039dfe2a5b01F3E1E6a2BBF9a576c6F95c4", #Curve d3pool Pool yVault (Curve d3pool)
        "0x23D3D0f1c697247d5e0a9efB37d8b0ED0C464f7f", #Curve tBTC Pool yVault (Curve tBTC)
        "0x801Ab06154Bf539dea4385a39f5fa8534fB53073", #Curve EURS-USDC Pool yVault (Curve EURS-USDC)
        "0xFD0877d9095789cAF24c98F7CCe092fa8E120775" #TUSD yVault (TUSD)
    ]
    vaults = []

    for x in range(0, len(yearnVaultList)):
        vaults.append(
            Contract.from_abi("Yearn Vault", yearnVaultList[x], interface.YearnVaultInterface.abi)
        )

    blockNumber = web3.eth.blockNumber

    vault_header = [
        "Vault Name",
        "Block Number",
        "Vault Asset",
        "price per share",
        "Total assets in vault"
        "Total Supply of Shares"
    ]
    
    fileName = "yearnInfo-multicall-eth-" + str(blockNumber) + ".csv"
    f = open(fileName, 'w')
    writer = csv.writer(f)
    writer.writerow(vault_header)
    
    names = []
    vaultAssets = []
    prices = []
    totalAssets =[]
    totalShares = []

    multicall(address="0x5BA1e12693Dc8F9c48aAD8770482f4739bEeD696")
    with multicall:
        for x in range(0, len(vaults)):
            name = vaults[x].name()
            asset = vaults[x].token()
            pps = vaults[x].pricePerShare()
            totalAsset = vaults[x].totalAssets()
            totalShare = vaults[x].totalSupply()
            names.append(name)
            vaultAssets.append(asset)
            prices.append(pps)
            totalAssets.append(totalAsset)
            totalShares.append(totalShare)
    

    for i in range(0, len(names)):
        data = [
            names[i],
            blockNumber,
            vaultAssets[i],
            prices[i],
            totalAssets[i],
            totalShares[i]
        ]
        writer.writerow(data)

            



