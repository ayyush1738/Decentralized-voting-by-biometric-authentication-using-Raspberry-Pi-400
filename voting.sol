// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.5.0 < 0.9.0;

contract vote{

    string[]  voterlist;
    uint public p1=0;
    uint public p2=0;
    uint public p3=0;

    constructor(){
        voterlist=["6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b",
        "d4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35",
        "4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce",
        "4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a",
        "ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d",
        "e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683",
        "7902699be42c8a8e46fbbb4501726517e86b22c56a189f7625a6da49081b2451",
        "2c624232cdd221771294dfbb310aca000a0df6ac8b66b696d90ef06fdefb64a3",
        "19581e27de7ced00ff1ce50b2047e7a567c76b1cbaebabe5ef03f7c3017bb5b7",
        "4a44dc15364204a80fe80e9039455cc1608281820fe2b24f1e5233ade6af1dd5"];

    }

    
    function verify(string memory id) public view returns(string memory){
        uint c=0;
        for(uint i=0;i<voterlist.length;i++){
            if(keccak256(abi.encodePacked(voterlist[i]))==keccak256(abi.encodePacked(id))){
                c++;
            }
        }
        if(c>0){
            return "Valid Voter";
        }
        else{
            return "Invalid Voter";
        }
    }

    function castvoteparty1(string memory id)public {
        for(uint i=0;i<voterlist.length;i++){
            if(keccak256(abi.encodePacked(voterlist[i]))==keccak256(abi.encodePacked(id))){
               voterlist[i]="000";
               p1++;
            }
        }
    }

    function castvoteparty2(string memory id)public {
        for(uint i=0;i<voterlist.length;i++){
            if(keccak256(abi.encodePacked(voterlist[i]))==keccak256(abi.encodePacked(id))){
               voterlist[i]="000";
               p2++;
            }
        }
    }

    function castvoteparty3(string memory id)public {
        for(uint i=0;i<voterlist.length;i++){
            if(keccak256(abi.encodePacked(voterlist[i]))==keccak256(abi.encodePacked(id))){
               voterlist[i]="000";
               p3++;
            }
        }
    }
    
    function arr()public view returns(string[] memory){
        return voterlist;
    }

}
