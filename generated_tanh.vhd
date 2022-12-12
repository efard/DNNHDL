
--tanh with saturation value: 5

LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;
USE IEEE.numeric_std.ALL;

entity my_tanh is
    port (i_data: in  std_logic_vector(7 downto 0);
          o_data: out std_logic_vector(15 downto 0));
end my_tanh;

architecture Behavioral of my_tanh is

  signal s_temp : signed(7 downto 0);

begin

  s_temp  <= signed(i_data);

  o_data  <= 
        std_logic_vector(to_signed(-32764,8)) 	when (s_temp = -5) 	 else
        std_logic_vector(to_signed(-32745,8)) 	when (s_temp = -4) 	 else
        std_logic_vector(to_signed(-32605,8)) 	when (s_temp = -3) 	 else
        std_logic_vector(to_signed(-31588,8)) 	when (s_temp = -2) 	 else
        std_logic_vector(to_signed(-24955,8)) 	when (s_temp = -1) 	 else
        std_logic_vector(to_signed(0,8)) 	when (s_temp = 0) 	 else
        std_logic_vector(to_signed(24955,8)) 	when (s_temp = 1) 	 else
        std_logic_vector(to_signed(31588,8)) 	when (s_temp = 2) 	 else
        std_logic_vector(to_signed(32605,8)) 	when (s_temp = 3) 	 else
        std_logic_vector(to_signed(32745,8)) 	when (s_temp = 4) 	 else
        std_logic_vector(to_signed(32764,8)) 	when (s_temp = 5) 	 else
        std_logic_vector(to_signed(32767,8)) 	when (s_temp >= 6) 	 else
        std_logic_vector(to_signed(-32768,8)); 	--for small inputs
end Behavioral;
