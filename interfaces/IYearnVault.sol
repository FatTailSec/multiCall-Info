// SPDX-Liscense-Identifier: MIT
pragma solidity ^0.8.0;

interface YearnVaultInterface {
    // Returns the underlying token of the vault 
    function token() external view returns(address);
    function totalAssets() external view returns(uint256);
    function totalSupply() external view returns(uint256);
    function pricePerShare() external view returns(uint256);
    function name() external view returns(string memory);
}