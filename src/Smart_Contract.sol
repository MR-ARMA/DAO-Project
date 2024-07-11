pragma solidity ^0.8.0;

contract CarBodyInsurance {
    struct Policy {
        // Details of the insured
        uint id;
        address holder;
        string policyholderName;
        string nationalCode;
        string addressAndPhone;
        string beneficiary;
        string insurancePolicyNumber;
        uint vehicleValue;

        // Details of the previous insurance policy
        bool thanksToPreviousInsurance;
        string previousInsurancePolicyNumber;
        string previousStartDate;
        string previousEndDate;
        string previousRiskHistory;
        string additionalRiskHistory;

        // Additional additional coverage
        string additionalCoverage;

        // Policy term
        string policyTerm;

        // Issuing unit
        string issuingUnit;

        // Vehicle specifications
        string vehicleType;
        string system;
        uint cylinder;
        string engineNumber;
        string plaque;
        string plateType;
        uint yearOfConstruction;
        bool used;
        string chassisNumber;
        uint capacity;

        // The value of installed parts and accessories
        uint partsAndAccessoriesValue;

        // Private conditions
        string privateConditions;

        // Insurance premium calculations
        uint premium;

        uint coverageAmount;
        bool isActive;
    }

    struct Claim {
        uint id;
        uint policyId;
        uint amount;
        bool isApproved;
    }

    uint public policyCount;
    uint public claimCount;
    mapping(uint => Policy) public policies;
    mapping(uint => Claim) public claims;
    mapping(address => uint) public tokenBalance;

    event PolicyCreated(uint policyId, address holder, uint premium, uint coverageAmount);
    event ClaimSubmitted(uint claimId, uint policyId, uint amount);
    event ClaimApproved(uint claimId, uint amount);
    event ClaimRejected(uint claimId);
    event TokensAssigned(address holder, uint amount);

    function createPolicy(
        string memory _policyholderName,
        string memory _nationalCode,
        string memory _addressAndPhone,
        string memory _beneficiary,
        string memory _insurancePolicyNumber,
        uint _vehicleValue,
        bool _thanksToPreviousInsurance,
        string memory _previousInsurancePolicyNumber,
        string memory _previousStartDate,
        string memory _previousEndDate,
        string memory _previousRiskHistory,
        string memory _additionalRiskHistory,
        string memory _additionalCoverage,
        string memory _policyTerm,
        string memory _issuingUnit,
        string memory _vehicleType,
        string memory _system,
        uint _cylinder,
        string memory _engineNumber,
        string memory _plaque,
        string memory _plateType,
        uint _yearOfConstruction,
        bool _used,
        string memory _chassisNumber,
        uint _capacity,
        uint _partsAndAccessoriesValue,
        string memory _privateConditions,
        uint _premium,
        uint _coverageAmount
    ) public {
        policyCount++;
        policies[policyCount] = Policy(
            policyCount,
            msg.sender,
            _policyholderName,
            _nationalCode,
            _addressAndPhone,
            _beneficiary,
            _insurancePolicyNumber,
            _vehicleValue,
            _thanksToPreviousInsurance,
            _previousInsurancePolicyNumber,
            _previousStartDate,
            _previousEndDate,
            _previousRiskHistory,
            _additionalRiskHistory,
            _additionalCoverage,
            _policyTerm,
            _issuingUnit,
            _vehicleType,
            _system,
            _cylinder,
            _engineNumber,
            _plaque,
            _plateType,
            _yearOfConstruction,
            _used,
            _chassisNumber,
            _capacity,
            _partsAndAccessoriesValue,
            _privateConditions,
            _premium,
            _coverageAmount,
            true
        );

        // Assign tokens to the policyholder
        uint tokens = calculateTokens(_premium);
        tokenBalance[msg.sender] += tokens;
        emit TokensAssigned(msg.sender, tokens);

        emit PolicyCreated(policyCount, msg.sender, _premium, _coverageAmount);
    }

    function submitClaim(uint _policyId, uint _amount) public {
        require(policies[_policyId].isActive, "Policy is not active");
        require(policies[_policyId].holder == msg.sender, "Only policy holder can submit a claim");
        claimCount++;
        claims[claimCount] = Claim(claimCount, _policyId, _amount, false);
        emit ClaimSubmitted(claimCount, _policyId, _amount);
    }

    function approveClaim(uint _claimId) public {
        Claim storage claim = claims[_claimId];
        Policy storage policy = policies[claim.policyId];
        require(policy.isActive, "Policy is not active");
        require(claim.amount <= policy.coverageAmount, "Claim amount exceeds coverage amount");
        claim.isApproved = true;
        emit ClaimApproved(_claimId, claim.amount);
        payable(policy.holder).transfer(claim.amount);
    }

    function rejectClaim(uint _claimId) public {
        Claim storage claim = claims[_claimId];
        claim.isApproved = false;
        emit ClaimRejected(_claimId);
    }

    function getTokenBalance(address _holder) public view returns (uint) {
        return tokenBalance[_holder];
    }

    function calculateTokens(uint _premium) internal pure returns (uint) {
        // Define the logic for calculating tokens based on the premium
        // For example, 1 token per 100 wei of premium
        return _premium / 100;
    }

    receive() external payable {}
}
