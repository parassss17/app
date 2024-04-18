-- Create the branches table
CREATE DATABASE courier_system;

CREATE TABLE branches (
  branch_id INT PRIMARY KEY,
  branch_name VARCHAR(100) NOT NULL,
  address VARCHAR(255) NOT NULL,
  contact_number VARCHAR(20) NOT NULL
);

-- Create the staffs table
CREATE TABLE staffs (
  staff_id INT PRIMARY KEY,
  branch_id INT,
  staff_name VARCHAR(100) NOT NULL,
  designation VARCHAR(100) NOT NULL,
  contact_number VARCHAR(20) NOT NULL,
  FOREIGN KEY (branch_id) REFERENCES branches(branch_id)
);

-- Create the parcels table
CREATE TABLE parcels (
  parcel_id INT PRIMARY KEY,
  sender_name VARCHAR(100) NOT NULL,
  receiver_name VARCHAR(100) NOT NULL,
  pickup_address VARCHAR(255) NOT NULL,
  delivery_address VARCHAR(255) NOT NULL,
  status VARCHAR(50) NOT NULL,
  staff_id INT,
  FOREIGN KEY (staff_id) REFERENCES staffs(staff_id)
);

-- Create the pricing table
CREATE TABLE pricing (
  state_from VARCHAR(100) NOT NULL,
  state_to VARCHAR(100) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (state_from, state_to)
);
