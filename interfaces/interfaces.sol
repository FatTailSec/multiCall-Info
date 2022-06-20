pragma solidity 0.8.3;

interface scriptInterface {
    function token() external view returns(address);
    function minter() external view returns(address);
    function totalAssets() external view returns(uint256);
    function calc_withdraw_one_coin(uint256, int128) external view returns(uint256);
    function calc_withdraw_one_coin(uint256, uint256) external view returns(uint256);
    function totalSupply() external view returns(uint256);
    function name() external view returns(string memory);
    function pricePerShare() external view returns(uint256);
}