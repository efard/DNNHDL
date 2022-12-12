
--sigmoid with saturation value: 5

LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;
USE IEEE.numeric_std.ALL;

entity my_sigmoid is
    port (i_data: in  std_logic_vector(7 downto 0);
          o_data: out std_logic_vector(15 downto 0));
end my_sigmoid;

architecture Behavioral of my_sigmoid is

  signal s_temp : signed(7 downto 0);

begin

  s_temp  <= signed(i_data);

  o_data  <= 
        std_logic_vector(to_signed(1,8)) 	when (s_temp = -11) 	 else
        std_logic_vector(to_signed(1,8)) 	when (s_temp = -10) 	 else
        std_logic_vector(to_signed(4,8)) 	when (s_temp = -9) 	 else
        std_logic_vector(to_signed(11,8)) 	when (s_temp = -8) 	 else
        std_logic_vector(to_signed(30,8)) 	when (s_temp = -7) 	 else
        std_logic_vector(to_signed(81,8)) 	when (s_temp = -6) 	 else
        std_logic_vector(to_signed(219,8)) 	when (s_temp = -5) 	 else
        std_logic_vector(to_signed(589,8)) 	when (s_temp = -4) 	 else
        std_logic_vector(to_signed(1554,8)) 	when (s_temp = -3) 	 else
        std_logic_vector(to_signed(3906,8)) 	when (s_temp = -2) 	 else
        std_logic_vector(to_signed(8812,8)) 	when (s_temp = -1) 	 else
        std_logic_vector(to_signed(16384,8)) 	when (s_temp = 0) 	 else
        std_logic_vector(to_signed(23955,8)) 	when (s_temp = 1) 	 else
        std_logic_vector(to_signed(28861,8)) 	when (s_temp = 2) 	 else
        std_logic_vector(to_signed(31213,8)) 	when (s_temp = 3) 	 else
        std_logic_vector(to_signed(32178,8)) 	when (s_temp = 4) 	 else
        std_logic_vector(to_signed(32548,8)) 	when (s_temp = 5) 	 else
        std_logic_vector(to_signed(32686,8)) 	when (s_temp = 6) 	 else
        std_logic_vector(to_signed(32737,8)) 	when (s_temp = 7) 	 else
        std_logic_vector(to_signed(32756,8)) 	when (s_temp = 8) 	 else
        std_logic_vector(to_signed(32763,8)) 	when (s_temp = 9) 	 else
        std_logic_vector(to_signed(32766,8)) 	when (s_temp = 10) 	 else
        std_logic_vector(to_signed(32766,8)) 	when (s_temp = 11) 	 else
        std_logic_vector(to_signed(32767,8)) 	when (s_temp >= 12) 	 else
        std_logic_vector(to_signed(0,8)); 	--for small inputs
end Behavioral;
