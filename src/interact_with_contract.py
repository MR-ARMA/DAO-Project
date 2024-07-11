# Purpose: Contains the Python script to interact with the deployed smart contract, including creating policies, submitting claims, and approving/rejecting claims.


from web3 import Web3

# Connect to the local blockchain
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
if not w3.is_connected():
    raise Exception("Failed to connect to the local blockchain")

# Use the first account from Ganache
w3.eth.defaultAccount = w3.eth.accounts[0]

# ABI of the CarBodyInsurance contract
abi = [
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_policyholderName",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_nationalCode",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_addressAndPhone",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_beneficiary",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_insurancePolicyNumber",
                "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "_vehicleValue",
                "type": "uint256"
            },
            {
                "internalType": "bool",
                "name": "_thanksToPreviousInsurance",
                "type": "bool"
            },
            {
                "internalType": "string",
                "name": "_previousInsurancePolicyNumber",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_previousStartDate",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_previousEndDate",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_previousRiskHistory",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_additionalRiskHistory",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_additionalCoverage",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_policyTerm",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_issuingUnit",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_vehicleType",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_system",
                "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "_cylinder",
                "type": "uint256"
            },
            {
                "internalType": "string",
                "name": "_engineNumber",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_plaque",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_plateType",
                "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "_yearOfConstruction",
                "type": "uint256"
            },
            {
                "internalType": "bool",
                "name": "_used",
                "type": "bool"
            },
            {
                "internalType": "string",
                "name": "_chassisNumber",
                "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "_capacity",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_partsAndAccessoriesValue",
                "type": "uint256"
            },
            {
                "internalType": "string",
                "name": "_privateConditions",
                "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "_premium",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_coverageAmount",
                "type": "uint256"
            }
        ],
        "name": "createPolicy",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_policyId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_amount",
                "type": "uint256"
            }
        ],
        "name": "submitClaim",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_claimId",
                "type": "uint256"
            }
        ],
        "name": "approveClaim",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_claimId",
                "type": "uint256"
            }
        ],
        "name": "rejectClaim",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_claimId",
                "type": "uint256"
            }
        ],
        "name": "getClaim",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "policyId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            },
            {
                "internalType": "bool",
                "name": "isApproved",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

# Address of the deployed contract
contract_address = '0xYourContractAddressHere'

# Create contract instance
car_body_insurance_contract = w3.eth.contract(address=contract_address, abi=abi)

# Create a new insurance policy
tx_hash = car_body_insurance_contract.functions.createPolicy(
    "Alireza Mahdizadeh",
    "989131111111",
    "123 Main St, 5",
    "Alireza Mahdizadeh",
    "POL123456",
    20000,
    True,
    "PREV123456",
    "2022-01-01",
    "2023-01-01",
    "No incidents",
    "Minor scratches",
    "Fire, Theft",
    "12 months",
    "Unit 1",
    "Sedan",
    "Model X",
    4,
    "ENG123456",
    "ABC123",
    "Standard",
    2020,
    False,
    "CHS123456",
    5,
    5000,
    "No special conditions",
    1500,
    10000
).transact()
w3.eth.waitForTransactionReceipt(tx_hash)
print("Policy created")

# Submit a claim
tx_hash = car_body_insurance_contract.functions.submitClaim(1, 5000).transact()
w3.eth.waitForTransactionReceipt(tx_hash)
print("Claim submitted")

# Approve a claim
tx_hash = car_body_insurance_contract.functions.approveClaim(1).transact()
w3.eth.waitForTransactionReceipt(tx_hash)
print("Claim approved")

# Retrieve information about a claim
claim = car_body_insurance_contract.functions.getClaim(1).call()
print(f'Claim ID: {claim[0]}, Policy ID: {claim[1]}, Amount: {claim[2]}, Approved: {claim[3]}')
