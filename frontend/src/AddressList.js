import React, {useState, useEffect} from 'react';

const AddressList = () => {
  const [listItems, setListItems] = useState([]);
  
  async function fetchData() {
    const backendUrl = 'http://localhost:5002/addresses';
    fetch(backendUrl)
    .then((response) => {
      return response.json()
    })
    .then((addresses) => {
      const formattedAddresses = addresses.map((address) => {
        console.log(`looking at ${address.userId} now`)
        return (
          <li key={`address_${address.street}`}>
            <h4>User: {address.userId}</h4>
            <span>{address.country} </span>
            <span>{address.street}</span>
          </li>
        );
      });

      setListItems(formattedAddresses);
    })
    .catch((error) => {
      console.log(error);
    });
  }

  useEffect(() => {

    fetchData();
  
  }, []);

  return (
    <div className="AddressList">
      <h2>User Addresses:</h2>
      <ul>{listItems}</ul>
    </div>
  );
};
  
export default AddressList;
