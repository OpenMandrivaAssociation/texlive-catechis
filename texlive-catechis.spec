# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/catechis
# catalog-date 2008-09-02 21:23:27 +0200
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-catechis
Version:	1.1
Release:	4
Summary:	Macros for typesetting catechisms
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/catechis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catechis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catechis.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catechis.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The macros include: - format for question-and-answer; -
comments on answers; - citations; - a specialised enumerate
which only operates in the catechism parts of a document. The
macros are all highly customisable.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/catechis/catechis.sty
%doc %{_texmfdistdir}/doc/latex/catechis/README
%doc %{_texmfdistdir}/doc/latex/catechis/catechis.pdf
%doc %{_texmfdistdir}/doc/latex/catechis/test.tex
#- source
%doc %{_texmfdistdir}/source/latex/catechis/catechis.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 750013
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 718013
- texlive-catechis
- texlive-catechis
- texlive-catechis
- texlive-catechis
- texlive-catechis

