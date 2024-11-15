----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:   
-- Design Name: 
-- Module Name:    top_module - Behavioral 
-- Project Name: 
-- Target Devices: 
-- Tool versions: 
-- Description: 
--
-- Dependencies: 
--
-- Revision: 
-- Revision 0.01 - File Created
-- Additional Comments: 
--
----------------------------------------------------------------------------------

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_signed.ALL;
use IEEE.numeric_std.ALL;

entity top_module is
    Port ( i_clk : in  STD_LOGIC;
           i_x : in  STD_LOGIC_VECTOR (15 downto 0);
           o_y : out  STD_LOGIC_VECTOR (15 downto 0));
end top_module;

architecture Behavioral of top_module is


--FXP16 FOR 4 SEG========================================================================================
    type my_array_int is array (0 to 3) of integer;
    constant c_slope: my_array_int := (8, 13, 13, 8);

    constant c_lat  : my_array_int := (1, 2226, 34996, 64510);
--FXP16 FOR 4 SEG========================================================================================

    signal s_sae: integer;
    signal s_y: std_logic_vector(31 downto 0);

begin

    s_sae   <= to_integer(unsigned(i_x(15 downto 14))); --4     Segment Address Encoder
    --s_sae <= to_integer(unsigned(i_x(15 downto 11))); --32    Segment Address Encoder
    --s_sae <= to_integer(unsigned(i_x(15 downto 9)));  --128   Segment Address Encoder
    --s_sae <= to_integer(unsigned(i_x(15 downto 8)));  --256   Segment Address Encoder
    --s_sae <= to_integer(unsigned(i_x(15 downto 6)));  --1024  Segment Address Encoder

    process (i_clk) is
    begin
        if rising_edge(i_clk) then
            s_y <= std_logic_vector(x"0000" & unsigned(i_x) sll c_slope(s_sae)) + c_lat(s_sae);
            o_y <= s_y(31 downto 16);
        end if;
    end process;
    

end Behavioral;

