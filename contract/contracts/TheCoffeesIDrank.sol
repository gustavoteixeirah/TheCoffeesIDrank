// SPDX-License-Identifier: MIT
pragma solidity 0.8.11;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TheCoffeesIDrank is ERC721Enumerable, Ownable {
    event PermanentURI(string _value, uint256 indexed _id);
    uint256 public tokenCount = 0;

    mapping(uint256 => string) private _tokenURIs;
    mapping(uint256 => bool) private _frozen;

    constructor() ERC721("The Coffees I Drank", "TCID") {}

    modifier notFrozen(uint256 _tokenId) {
        require(!_frozen[_tokenId]);
        _;
    }

    modifier exist(uint256 _tokenId) {
        require(_exists(_tokenId), "URI query for nonexistent token");
        _;
    }

    function tokenURI(uint256 _tokenId)
        public
        view
        virtual
        override
        exist(_tokenId)
        returns (string memory)
    {
        return _tokenURIs[_tokenId];
    }

    function mint(string memory _tokenURI) public onlyOwner {
        _safeMint(msg.sender, getNextTokenId());
        _tokenURIs[tokenCount] = _tokenURI;
    }

    function mintAndFreeze(string memory _tokenURI) public onlyOwner {
        _safeMint(msg.sender, getNextTokenId());
        updateTokenURIAndfreeze(_tokenURI, tokenCount);
    }

    function getNextTokenId() private returns (uint256) {
        tokenCount += 1;
        return tokenCount;
    }

    function updateTokenURI(string memory _newTokenUri, uint256 _tokenId)
        public
        onlyOwner
        exist(_tokenId)
        notFrozen(_tokenId)
    {
        _tokenURIs[_tokenId] = _newTokenUri;
    }

    function updateTokenURIAndfreeze(string memory _tokenURI, uint256 _tokenId)
        public
        exist(_tokenId)
        notFrozen(_tokenId)
        onlyOwner
    {
        _tokenURIs[_tokenId] = _tokenURI;
        _frozen[_tokenId] = true;
        emit PermanentURI(_tokenURI, _tokenId);
    }

    function justFreeze(uint256 _tokenId)
        public
        exist(_tokenId)
        notFrozen(_tokenId)
        onlyOwner
    {
        _frozen[_tokenId] = true;
        emit PermanentURI(_tokenURIs[_tokenId], _tokenId);
    }
}
